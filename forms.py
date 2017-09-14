from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserModelForm(form.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength':255}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength':32}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength':32}),

        }
        erros_messages = {
            'username': {
                'required': 'Este campo é obrigatório'
            },
            'email': {
                'required': 'Este campo é obrigatório'
            },
            'password': {
                'required': 'Este campo é obrigatório'
            },
            'confirm_password': {
                'required': 'Este campo é obrigatório'
            },
        }
