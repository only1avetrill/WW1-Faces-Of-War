from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import FormMixin

from .models import *
from .forms import *

from django.views.generic import DetailView
from django.core.paginator import Paginator

#Служебные функции
from django.contrib.auth import logout

def Home(request):
    article_list = Article.objects.order_by('-creation_date')
    p = Paginator(Article.objects.order_by('-creation_date'), 3)
    page = request.GET.get('page')
    article_page = p.get_page(page)

    data = {
        'article_list': article_list,
        'article_page': article_page
    }
    return render(request, 'home.html', data)

def FacesOfWar(request):
    faces = Face.objects.all()

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



#Добавление
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

def AddArticlePage(request):
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







#Служебные функции
def Logout(request):
    logout(request)
    return redirect('home')

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def Quotes(request):
    quote_list = Quote.objects.all()

    data = {
        'quote_list': quote_list,
    }
    return render(request, 'quotes.html', data)


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