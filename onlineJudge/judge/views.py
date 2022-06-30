from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse


from .models import Problem


def index(request):
    latest_question_list = Problem.objects.order_by('difficulty')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'judge/index.html', context)

def detail(request, problemId):
    problem = get_object_or_404(Problem, pk=problemId)
    return render(request, 'judge/detail.html', {'problem': problem})