# Generated by Django 2.0 on 2019-04-23 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='data_atualizacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='data_criacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]