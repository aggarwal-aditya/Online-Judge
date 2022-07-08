from dataclasses import dataclass
import datetime
import filecmp
from itertools import tee
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.http import HttpResponse
import os

# from onlineJudge import judge


from .models import Problem, Submission, TestCase


def index(request):
    return render(request, 'judge/index.html')


def problem(request):
    latest_question_list = Problem.objects.order_by('difficulty')
    page = request.GET.get('page', 1)
    paginator = Paginator(latest_question_list, 2)
    try:
        latest_question_list = paginator.page(page)
    except PageNotAnInteger:
        latest_question_list = paginator.page(1)
    except EmptyPage:
        latest_question_list = paginator.page(paginator.num_pages)
    return render(request, 'judge/problems.html', {'latest_question_list': latest_question_list})


def detail(request, problemId):
    problem = get_object_or_404(Problem, pk=problemId)
    return render(request, 'judge/detail.html', {'problem': problem})


def submit(request, problemId):
    f = request.FILES['solution'].read()
    path = r'solutions/code.'
    path = path+request.POST["lang"]
    sol_file = open(path, "wb")
    sol_file.write(f)
    sol_file.close()
    problem = Problem.objects.get(pk=problemId)
    testcase = TestCase.objects.filter(problem=problem)
    soln = Submission()
    soln.problem = problem
    soln.pub_date = datetime.datetime.now()
    for test in testcase.iterator():
        f = test.expectedInput
        inp_file = open("solutions/input.txt", "w")
        inp_file.write(f)
        inp_file.close()
        f = test.expectedOutput
        out_file = open("solutions/output.txt", "w")
        out_file.write(f)
        out_file.close()
        os.system('g++ solutions/code.cpp')
        if(not os.path.exists("a.out")):
            verdict = "Compilation Error"
            soln.verdict = verdict
            soln.save()
            return render(request, 'judge/submissions.html', {'verdict': verdict})
        else:
            os.system('./a.out < solutions/input.txt >solutions/out.txt')
            if(filecmp.cmp('solutions/output.txt', 'solutions/out.txt', shallow=False)):
                verdict = "Accepted"
            else:
                if os.path.exists("a.out"):
                    os.remove("a.out")
                if os.path.exists("solutions/input.txt"):
                    os.remove("solutions/input.txt")
                if os.path.exists("solutions/out.txt"):
                    os.remove("solutions/out.txt")
                if os.path.exists("solutions/output.txt"):
                    os.remove("solutions/output.txt")
                verdict = "Wrong Answer"
                soln.verdict = verdict
                soln.save()
                return render(request, 'judge/submissions.html', {'verdict': verdict})
        soln.verdict = verdict
        if os.path.exists("a.out"):
            os.remove("a.out")
        if os.path.exists("solutions/input.txt"):
            os.remove("solutions/input.txt")
        if os.path.exists("solutions/out.txt"):
            os.remove("solutions/out.txt")
        if os.path.exists("solutions/output.txt"):
            os.remove("solutions/output.txt")
    problem.solveCount = problem.solveCount+1
    problem.save()
    soln.save()
    return render(request, 'judge/submissions.html', {'verdict': verdict})


def submission(request):
    return render(request, 'judge/submissions.html')


def customtest(request):
    return render(request, 'judge/customtest.html')
