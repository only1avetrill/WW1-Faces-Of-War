# Generated by Django 4.0.4 on 2022-05-31 13:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_article_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Текст статьи'),
        ),
    ]
