from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
import os

# from onlineJudge import judge


from .models import Problem


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
    inp_file = open("solutions/input.txt", "wb")
    problem = get_object_or_404(Problem, pk=problemId)
    f = problem.expectedInput
    inp_file.write(f)
    inp_file.close()
    os.system('g++ solutions/code.cpp')

    if os.path.exists("a.out"):
        os.remove("a.out")
    if os.path.exists("a.exe"):
        os.remove("a.exe")
    return redirect('/judge/submissions')


def submission(request):
    return render(request, 'judge/submissions.html')
