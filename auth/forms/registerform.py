# -*- coding: utf-8 -*-
from django import forms


class RegisterForm(forms.Form):

    first_name = forms.CharField(label='Primeiro Nome', max_length=100, required=True)
    last_name = forms.CharField(label='Sobrenome', max_length=100, required=True)
    username = forms.CharField(label='Usuário', max_length=100, required=True)
    email = forms.EmailField(label='E-mail', max_length=255, required=True)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(), min_length=6, required=True)
