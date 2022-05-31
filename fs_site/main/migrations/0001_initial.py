# Generated by Django 4.0.4 on 2022-05-31 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('country', models.CharField(max_length=300, verbose_name='Нация')),
                ('rank', models.CharField(max_length=300, verbose_name='Должность')),
                ('army', models.CharField(max_length=300, verbose_name='Род войск')),
                ('biography', models.TextField(blank=True, verbose_name='Краткая биография')),
                ('photo', models.CharField(max_length=300, verbose_name='Ссылка на фото')),
                ('lifetime_start', models.CharField(max_length=4, verbose_name='Год рождения')),
                ('lifetime_end', models.CharField(max_length=4, verbose_name='Год смерти')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Личность',
                'verbose_name_plural': 'Личности',
            },
        ),
        migrations.CreateModel(
            name='FaceComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=1000, verbose_name='Текст')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='face_comment', to='main.face', verbose_name='Личность')),
            ],
            options={
                'verbose_name': 'Комментарий личности',
                'verbose_name_plural': 'Комментарии личности',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Статья')),
                ('snippet', models.CharField(max_length=5000, verbose_name='Сниппет')),
                ('text', models.TextField(verbose_name='Текст')),
                ('creation_date', models.DateTimeField(verbose_name='Дата и время создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
