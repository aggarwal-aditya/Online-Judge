import filecmp
from itertools import tee
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
import os

# from onlineJudge import judge


from .models import Problem, TestCase


def index(request):
    return render(request, 'judge/index.html')


def problem(request):
    latest_question_list = Problem.objects.order_by('difficulty')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'judge/problems.html', context)


def detail(request, problemId):
    problem = get_object_or_404(Problem, pk=problemId)
    return render(request, 'judge/detail.html', {'problem': problem})


def submit(request, problemId):
    f = request.FILES['solution'].read()
    sol_file = open("solutions/code.cpp", "wb")
    sol_file.write(f)
    sol_file.close()
    problem=Problem.objects.get(pk=problemId)
    testcase = TestCase.objects.get (pk=problemId)
    # print(type(testca))
    f = testcase.expectedInput
    inp_file = open("solutions/input.txt", "w")
    inp_file.write(f)
    inp_file.close()
    f = testcase.expectedOutput
    out_file = open("solutions/output.txt", "w")
    out_file.write(f)
    out_file.close()
    os.system('g++ solutions/code.cpp')
    os.system('./a.out < solutions/input.txt >solutions/out.txt')
    if(filecmp.cmp('solutions/output.txt', 'solutions/out.txt', shallow=False)):
        verdict = "Accepted"
    else:
        verdict = "Wrong Answer"
    print(verdict)
    if os.path.exists("a.out"):
        os.remove("a.out")
    if os.path.exists("a.exe"):
        os.remove("a.exe")
    if os.path.exists("solutions/input.txt"):
        os.remove("solutions/input.txt")
    if os.path.exists("solutions/out.txt"):
        os.remove("solutions/out.txt")
    if os.path.exists("solutions/output.txt"):
        os.remove("solutions/output.txt")
    return redirect('/judge/submissions')


def submission(request):
    return render(request, 'judge/submissions.html')
