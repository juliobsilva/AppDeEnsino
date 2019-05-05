from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    template_name = 'core/home.html'
    return render(request, template_name)

def contato(request):
    template_name = 'core/contato.html'
    return render(request, template_name)
