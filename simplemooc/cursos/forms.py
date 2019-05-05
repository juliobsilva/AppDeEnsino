from django import forms
from django.core.mail import send_mail
from django.conf import settings
from simplemooc.core.mail import send_mail_template

class ContatoCursoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    menssagem = forms.CharField(
        label='Menssagem/Dúvida', widget=forms.Textarea
    )


    def send_mail(self, curso):
        subject = '[%s] Contato' % curso
        message = 'Nome: %(nome)s;E-mail: %(email)s;%(menssagem)s'
        context = {
            'nome': self.cleaned_data['nome'],
            'email': self.cleaned_data['email'],
            'menssagem': self.cleaned_data['menssagem'],
        }
        template_name = 'cursos/contato_email.html'
        send_mail_template(
                subject, template_name, context, [settings.CONTATO_EMAIL]
        )
