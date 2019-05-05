from django.urls import path, include
from .views import home, contato

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('contato', contato, name='contato')
]
