import re
from django.shortcuts import render
from dataclasses import dataclass
import datetime
import filecmp
from itertools import tee
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.http import HttpResponse
import os


def signup(request):
    return render(request, 'accounts/register.html')
