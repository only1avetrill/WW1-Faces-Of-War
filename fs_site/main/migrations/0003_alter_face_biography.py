# Generated by Django 4.0.4 on 2022-05-31 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_face_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='biography',
            field=models.TextField(blank=True, verbose_name='Краткая биография'),
        ),
    ]
