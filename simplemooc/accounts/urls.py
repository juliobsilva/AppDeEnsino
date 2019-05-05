#from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from simplemooc.accounts.views import(
registro,
dashboard,
editar,
editar_senha,
password_reset,
password_reset_confirm,

)


app_name = 'accounts'

urlpatterns = [
    #path('entrar', include('django.contrib.auth.urls'), {'template_name': 'login.html'}, name='login'),
    path('entrar/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='login'
        ),
    path('sair/', auth_views.LogoutView.as_view(
        template_name='core:home'), name='logout'
        ),

    path('cadastre-se/', registro, name='registro'),
    path('nova-senha/', password_reset, name='password_reset'),
    re_path('confirmar-nova-senha/(?P<key>\w+)/$', password_reset_confirm, name='password_reset_confirm'),

    path('dashboard/', dashboard, name='dashboard'),
    path('editar/', editar, name='editar'),
    path('editar-senha/', editar_senha, name='editar_senha'),


]
