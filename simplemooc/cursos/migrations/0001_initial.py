# Generated by Django 2.0 on 2019-04-23 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('descricao', models.TextField(blank=True)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='imgcursos')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('data_atualizacao', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
    ]