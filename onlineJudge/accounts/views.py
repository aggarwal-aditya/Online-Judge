import email
import re
from django.shortcuts import render
from dataclasses import dataclass
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signup(request):
    return render(request, 'accounts/register.html')


def register(request):
    handle = request.POST['handle']
    email = request.POST['email']
    psw = request.POST['psw']
    try:
        user = User.objects.get(username=handle)
        context = {
            'error': 'The username you entered has already been taken. Please try another username.'}
        return render(request, 'accounts/register.html', context)
    except User.DoesNotExist:
        user = User.objects.create_user(handle, password=psw, email=email)
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('/judge')


def login_page(request):
    return render(request, 'accounts/login.html')


def signin(request):
    handle = request.POST['handle']
    psw = request.POST['psw']
    user = user = authenticate(request, username=handle, password=psw)
    if user is not None:
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    else:
        context = {
            'error': 'Invalid username/password'}
        return render(request, 'accounts/login.html', context)
    return redirect('/judge')
