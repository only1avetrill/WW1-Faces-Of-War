# Generated by Django 4.0.4 on 2022-05-31 10:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_face_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='biography',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Краткая биография'),
        ),
    ]