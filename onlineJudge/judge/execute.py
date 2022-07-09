import datetime
import filecmp
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import HttpResponse
import epicbox
from .models import *
from celery import Celery, shared_task

limits = {'cputime': 2, 'memory': 256}

PROFILES = []
for language in ProgrammingLanguage.objects.all():
    PROFILES.append(epicbox.Profile(
        language.name, language.dockerImage, None, 'root', False, True))
epicbox.configure(profiles=PROFILES)


@shared_task(acks_late=True)
def submit(queueid):
    def execute(request, problemId):
        userCode = request.FILES['solution'].read()
        problem = Problem.objects.get(pk=problemId)
        testCase = TestCase.objects.filter(problem=problem)
