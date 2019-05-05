from django.urls import path, include



from .views import curso_index, curso_detalhe

app_name = 'cursos'
urlpatterns = [
    #path('', home, name='home')
    path('cursoindex', curso_index, name='cursoindex'),
    path('cursodetalhe/<slug:slug>/', curso_detalhe, name='cursodetalhe')

]
