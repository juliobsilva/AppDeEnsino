from django.contrib import admin

from .models import Curso


class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'data_inicio', 'data_criacao']
    search_fields = ['nome', 'slug']
    prepopulated_fields = {"slug": ("nome",)}

admin.site.register(Curso, CursoAdmin)
