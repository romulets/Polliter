# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from forms.registerform import RegisterForm
from django.contrib.auth.views import login as django_login
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'user/templates/home.html', {
        'pageTitle': 'Minhas Notícias',
        'jsController': 'PrivateTopicsController',
    })


@login_required
def all(request):
    return render(request, 'user/templates/home.html', {
        'pageTitle': 'Últimas Notícias',
        'jsController': 'PublicTopicsController',
    })


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('home')
    else:
        return django_login(request, template_name='user/templates/login.html')


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            return HttpResponseRedirect('home')

    form = RegisterForm
    return render(request, 'user/templates/register.html', {
        'form': form
    })
