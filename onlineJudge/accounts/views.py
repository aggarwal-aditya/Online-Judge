import email
import re
from django.shortcuts import render
from dataclasses import dataclass
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.contrib.auth.models import User
import os


def signup(request):
    return render(request, 'accounts/register.html')


def register(request):
    handle = request.POST['handle']
    email = request.POST['email']
    psw = request.POST['psw']
    try:
        user = User.objects.get(username=handle)
    except User.DoesNotExist:
        user = User.objects.create_user(handle, password=psw, email=email)
        user.save()
    return render(request, 'judge/problems.html')
