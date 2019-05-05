from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.forms import(
UserCreationForm,
PasswordChangeForm,
SetPasswordForm,
)
from django.contrib.auth import authenticate, login, get_user_model
from simplemooc.accounts.models import User
from django.contrib.auth.decorators import login_required

from simplemooc.core.utils import generate_hash_key

from .forms import RegistroForm, EditeContaForm, PasswordResetForm
from django.conf import settings
from .models import PasswordReset

User = get_user_model()

def registro(request):
    template_name = 'accounts/registro.html'
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('core:home')

            return redirect('accounts:login')
    else:
        form = RegistroForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

def password_reset(request):
    template_name = 'accounts/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['sucesso'] = True
    context['form'] = form
    return render(request, template_name, context)

def password_reset_confirm(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_list_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['sucesso'] = True
    context['form'] = form
    return render(request, template_name, context)

@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)


@login_required
def editar(request):
    template_name = 'accounts/editar.html'
    context = {}
    if request.method == 'POST':
        form = EditeContaForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditeContaForm(instance=request.user)
            context['sucesso'] = True
    else:
        form = EditeContaForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def editar_senha(request):
    template_name = 'accounts/editar_senha.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['sucesso'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)
