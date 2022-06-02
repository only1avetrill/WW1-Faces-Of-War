from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.forms import ModelForm, TextInput, Textarea, Select, EmailField
from django.contrib.auth.models import User
from django import forms
from .models import *


class AuthForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'style': 'height: 40px',
               'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'style': 'height: 40px',
            'placeholder': 'Пароль'}))

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'style': 'height: 40px',
               'placeholder': 'Имя пользователя'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'style': 'height: 40px',
            'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'style': 'height: 40px',
            'placeholder': 'Повторите пароль'}))
    first_name = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'style': 'height: 40px',
               'placeholder': 'Имя'}))
    last_name = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'style': 'height: 40px',
               'placeholder': 'Фамилия'}))
    email = EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'style': 'height: 40px',
               'placeholder': 'Электронная почта'}))

class AddFaceForm(ModelForm):
    class Meta:
        model = Face
        fields = ['name', 'type', 'country', 'rank', 'army', 'army_part', 'biography', 'photo', 'lifetime_start', 'lifetime_end', 'author']

        widgets = {
            'name':TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Имя, фамилия, отчество и т.д.',
            }),
            'country': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Страна (принадлежность)',
            }),
            'rank': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Звание (должность)',
            }),
            'type': Select(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Тип',
            }),
            'army': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Армия',
            }),
            'army_part': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Род войск',
            }),
            'biography': Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Биография',
            }),
            'photo': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Фото',
            }),
            'lifetime_start': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Год рождения',
            }),
            'lifetime_end': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Год смерти',
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'username_author',
                'type': 'hidden',
            })
        }

class FaceCommentForm(ModelForm):
    class Meta:
        model = FaceComment
        fields = ['text', 'author', 'face']

        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Текст комментария до 1000 символов...',
            }),
            'face': TextInput(attrs={
                'type': 'hidden',
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'username_author',
                'type': 'hidden',
            })
        }

class AddArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'snippet', 'text', 'author']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Название статьи',
            }),
            'snippet': Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Текст сниппета до 5000 символов...',
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'username_author',
                'type': 'hidden',
            })
        }

class AddQuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['text', 'photo', 'date', 'place', 'source', 'real_author', 'author', 'type']

        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Текст цитаты',
            }),
             'photo': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Фото',
            }),
            'date': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Год',
            }),
            'place': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Место',
            }),
            'source': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Источник',
            }),
            'real_author': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Автор',
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'username_author',
                'type': 'hidden',
            }),
            'type': Select(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Тип',
            }),
        }