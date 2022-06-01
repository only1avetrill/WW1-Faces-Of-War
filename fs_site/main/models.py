from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Article(models.Model):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    title = models.CharField(max_length=100, verbose_name='Статья')
    snippet = models.CharField(max_length=5000, verbose_name='Сниппет')
    text = RichTextField(verbose_name='Текст статьи', null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')


class Face(models.Model):
    type = (
        ('Гражданский', 'Гражданский'),
        ('Военный', 'Военный')
    )

    class Meta:
        verbose_name = 'Личность'
        verbose_name_plural = 'Личности'

    name = models.CharField(max_length=100, verbose_name='Имя')
    country = models.CharField(max_length=300, verbose_name='Нация')
    rank = models.CharField(max_length=300, verbose_name='Должность')
    army = models.CharField(max_length=300, verbose_name='Армия')
    type = models.CharField(max_length=300, verbose_name='Тип', choices = type)
    army_part = models.CharField(blank=True, max_length=300, verbose_name='Род войск')
    biography = models.TextField(blank=True, verbose_name='Краткая биография')
    photo = models.CharField(max_length=300, verbose_name='Ссылка на фото')
    lifetime_start = models.CharField(max_length=4, verbose_name='Год рождения')
    lifetime_end = models.CharField(max_length=4, verbose_name='Год смерти')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return self.name

class FaceComment(models.Model):
    class Meta:
        verbose_name = 'Комментарий личности'
        verbose_name_plural = 'Комментарии личности'

    text = models.CharField(max_length=1000, blank=True, verbose_name='Текст')
    face = models.ForeignKey(Face, on_delete=models.CASCADE, verbose_name='Личность', related_name='face_comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

class Quote(models.Model):
    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

    text = models.TextField(verbose_name='Текст')
    photo = models.CharField(max_length=300, verbose_name='Ссылка на фото')
    date = models.CharField(blank=True, max_length=4, verbose_name='Год')
    place = models.TextField(blank=True, verbose_name='Место')
    source = models.TextField(blank=True, verbose_name='Источник')
    real_author = models.TextField(blank=True, verbose_name='Реальный автор')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return self.text

class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField(max_length=100, verbose_name='Новость')
    snippet = models.CharField(max_length=5000, verbose_name='Сниппет')
    text = RichTextField(verbose_name='Текст новости', null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')


