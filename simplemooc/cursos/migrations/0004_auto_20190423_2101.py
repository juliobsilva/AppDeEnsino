# Generated by Django 2.0 on 2019-04-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_auto_20190423_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='descricao_longa',
            field=models.TextField(blank=True, verbose_name='Sobre o Curso'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imgcursos'),
        ),
    ]