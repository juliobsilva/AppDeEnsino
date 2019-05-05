from django.db import models

class CursoManager(models.Manager):
    def pesquisa(self, query):
        return self.get_queryset().filter(
            nome__icontains=query, descricao__icontains=query
        )


class Curso(models.Model):

    nome = models.CharField(max_length=100)
    slug = models.SlugField('Atalho')
    descricao = models.TextField(blank=True)
    descricao_longa = models.TextField('Sobre o Curso', blank=True)
    data_inicio = models.DateField(
        null=True, blank=True
    )
    image = models.ImageField(upload_to='imgcursos', blank=True, null=True)

    data_criacao = models.DateTimeField(
        auto_now_add=True, blank=True, null=True
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True, blank=True, null=True
    )

    def __str__(self):

        return self.nome

    objects = CursoManager()
