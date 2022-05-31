from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django import forms
from .models import *

class AddFaceForm(ModelForm):
    class Meta:
        model = Face
        fields = ['name', 'country', 'rank', 'army', 'army_part', 'biography', 'photo', 'lifetime_start', 'lifetime_end', 'author']

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
        fields = ['text', 'photo', 'date', 'place', 'source', 'real_author', 'author']

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
            })
        }