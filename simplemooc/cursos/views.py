from django.shortcuts import render, get_object_or_404
from .models import Curso
from .forms import ContatoCursoForm

def curso_index(request):
    cursos = Curso.objects.all()
    data = {'cursos': cursos}
    return render(request, 'cursos/curso_index.html', data)

def curso_detalhe(request, slug):
    cursos = get_object_or_404(Curso, slug=slug)
    data = {}
    if request.method == 'POST':
        forms = ContatoCursoForm(request.POST)
        if forms.is_valid():
            data['is_valid'] = True
            forms.send_mail(cursos)
            print(forms.cleaned_data)
            forms = ContatoCursoForm()

    else:
        forms = ContatoCursoForm()

    data['cursos'] = cursos
    data['forms'] = forms

    return render(request, 'cursos/curso_detalhe.html', data)
