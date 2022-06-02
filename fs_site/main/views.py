import random
from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Max
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import FormMixin
from online_users.models import OnlineUserActivity

from .models import *
from .forms import *

from django.views.generic import DetailView
from django.core.paginator import Paginator

# Служебные функции
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def Home(request):
    article_list = Article.objects.order_by('-creation_date')
    p = Paginator(Article.objects.order_by('-creation_date'), 3)
    page = request.GET.get('page')
    article_page = p.get_page(page)

    max_id = QuoteOfTheDay.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id)
    quote = QuoteOfTheDay.objects.get(pk=pk)

    data = {
        'article_list': article_list,
        'article_page': article_page,
        'quote': quote
    }
    return render(request, 'home.html', data)


def Main(request):
    return redirect('home')


def FacesOfWar(request):
    faces = Face.objects.order_by('?')

    search = request.GET.get('search', '')
    if search:
        faces = Face.objects.filter(name__icontains=search)

    data = {
        'face': faces,
    }
    return render(request, 'facesofwar.html', data)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detailview.html'


class FacesOfWarDetailView(FormMixin, DetailView):
    model = Face
    template_name = 'facesofwar_detailview.html'
    form_class = FaceCommentForm

    def get_success_url(self):
        return reverse('face_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(FacesOfWarDetailView, self).get_context_data(**kwargs)
        context['form'] = FaceCommentForm(initial={'face': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(FacesOfWarDetailView, self).form_valid(form)


# Добавление
@login_required
def AddFacePage(request):
    if request.method == 'POST':
        form = AddFaceForm(request.POST)
        author = request.user.username
        if form.is_valid():
            form.save()
            return redirect('faces_of_war')
        else:
            return redirect('add_face')
        super(Event, self).save(*args, **kwargs)

    form = AddFaceForm
    data = {
        'form': form,
    }
    return render(request, 'add_face.html', data)

@login_required
def AddArticlePage(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AddArticleForm(request.POST)
            author = request.user.username
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                return redirect('add_article')
            super(Event, self).save(*args, **kwargs)

        form = AddArticleForm
        data = {
            'form': form,
        }
    else:
        raise Http404
    return render(request, 'add_article.html', data)


@login_required
def DeleteFace(request, id):
    face = Face.objects.get(id=id)

    if face.author == request.user:
        face.delete()
    elif request.user.is_superuser:
        face.delete()
    else:
        raise Http404

    return redirect('faces_of_war')


@login_required
def DeleteArticle(request, id):
    article = Article.objects.get(id=id)

    if article.author == request.user:
        article.delete()
    elif request.user.is_superuser:
        article.delete()
    else:
        raise Http404

    return redirect('home')


@login_required
def EditFace(request, id):
    face = Face.objects.get(id=id)
    form = AddFaceForm(instance=face)

    if face.author == request.user:
        if request.method == 'POST':
            form = AddFaceForm(request.POST, instance=face)
            if form.is_valid():
                form.save()
                return redirect('face_detail', id)
            else:
                return redirect('home')
            super(Event, self).save(*args, **kwargs)
    elif request.user.is_superuser:
        if request.method == 'POST':
            form = AddFaceForm(request.POST, instance=face)
            if form.is_valid():
                form.save()
                return redirect('face_detail', id)
            else:
                return redirect('home')
            super(Event, self).save(*args, **kwargs)
    else:
        raise Http404

    data = {
        'form': form,
    }

    return render(request, 'edit_face.html', data)


@login_required
def EditArticle(request, id):
    article = Article.objects.get(id=id)
    form = AddArticleForm(instance=article)

    if article.author == request.user:
        if request.method == 'POST':
            form = AddArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('article_detail', id)
            else:
                return redirect('home')
            super(Event, self).save(*args, **kwargs)
    elif request.user.is_superuser:
        if request.method == 'POST':
            form = AddArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('article_detail', id)
            else:
                return redirect('home')
            super(Event, self).save(*args, **kwargs)
    else:
        raise Http404

    data = {
        'form': form,
    }

    return render(request, 'edit_article.html', data)


# Служебные функции
def Logout(request):
    logout(request)
    return redirect('home')

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)

def About(request):
    faces_count = Face.objects.count()
    faces_count_military = Face.objects.filter(type__contains='Военный').count()
    faces_count_civil = Face.objects.filter(type__contains='Гражданский').count()

    quote_count = Quote.objects.count()
    quote_count_literature = Quote.objects.filter(type__contains='Литература').count()
    quote_count_document = Quote.objects.filter(type__contains='Документ').count()
    quote_count_memories = Quote.objects.filter(type__contains='Воспоминания').count()

    user_activity_objects = OnlineUserActivity.get_user_activities((timedelta(minutes=3)))
    number_of_active_users = user_activity_objects.count()

    comments_count = FaceComment.objects.count()
    all_count = (faces_count + quote_count)
    users_count = User.objects.count()

    data = {
        'faces_count': faces_count,
        'faces_count_military': faces_count_military,
        'faces_count_civil': faces_count_civil,
        'quote_count': quote_count,
        'quote_count_literature': quote_count_literature,
        'quote_count_document': quote_count_document,
        'quote_count_memories': quote_count_memories,
        'all_count': all_count,
        'comments_count': comments_count,
        'users_count': users_count,
        'online_users': number_of_active_users,
    }
    return render(request, 'about.html', data)


def Quotes(request):
    quote = Quote.objects.order_by('?')

    data = {
        'quote': quote,
    }
    return render(request, 'quotes.html', data)

@login_required
def AddQuotePage(request):
    if request.method == 'POST':
        form = AddQuoteForm(request.POST)
        author = request.user.username
        if form.is_valid():
            form.save()
            return redirect('quotes')
        else:
            return redirect('add_quote')
        super(Event, self).save(*args, **kwargs)

    form = AddQuoteForm
    data = {
        'form': form,
    }
    return render(request, 'add_quote.html', data)


def FacesOfWarFrance(request):
    faces = Face.objects.filter(country__icontains='Франция')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)
def FacesOfWarRussia(request):
    faces = Face.objects.filter(country__icontains='Российская империя')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)
def FacesOfWarGreatBritain(request):
    faces = Face.objects.filter(country__icontains='Великобритания')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)
def FacesOfWarUSA(request):
    faces = Face.objects.filter(country__icontains='США')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)
def FacesOfWarSerbia(request):
    faces = Face.objects.filter(country__icontains='Сербия')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)
def FacesOfWarBelgium(request):
    faces = Face.objects.filter(country__icontains='Бельгия')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)
def FacesOfWarItaly(request):
    faces = Face.objects.filter(country__icontains='Италия')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)
def FacesOfWarGermany(request):
    faces = Face.objects.filter(country__icontains='Германская империя')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)
def FacesOfWarAustriaHungary(request):
    faces = Face.objects.filter(country__icontains='Австро-Венгрия')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)
def FacesOfWarOttoman(request):
    faces = Face.objects.filter(country__icontains='Османская империя')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)
def FacesOfWarBulgary(request):
    faces = Face.objects.filter(country__icontains='Болгария')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)
def Combatants(request):
    faces = Face.objects.filter(type__icontains='Военный')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)
def NonCombatants(request):
    faces = Face.objects.filter(type__icontains='Гражданский')
    data = {'face': faces}
    return render(request, 'facesofwar.html', data)

def QuotesLiterature(request):
    quotes = Quote.objects.filter(type__icontains='Литература')
    data = {'quote': quotes}
    return render(request, 'quotes.html', data)
def QuotesDocument(request):
    quotes = Quote.objects.filter(type__icontains='Документ')
    data = {'quote': quotes}
    return render(request, 'quotes.html', data)
def QuotesMemories(request):
    quotes = Quote.objects.filter(type__icontains='Воспоминания')
    data = {'quote': quotes}
    return render(request, 'quotes.html', data)


def NewsPage(request):
    news_list = News.objects.all()
    p = Paginator(News.objects.all(), 3)
    page = request.GET.get('page')
    news_page = p.get_page(page)

    data = {
        'news_list': news_list,
        'news_page': news_page
    }
    return render(request, 'news.html', data)


def Auth(request):
    form = AuthForm
    data = {'form': form}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, 'Неверный логин или пароль!')
            return render(request, 'auth.html', data)
    else:
        user = request.user
        if user.is_authenticated:
            return redirect('home')
        return render(request, 'auth.html', data)

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})