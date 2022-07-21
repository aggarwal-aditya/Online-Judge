import datetime
import filecmp
from sys import stdin
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.http import HttpResponse
import epicbox
from .models import *
from django.contrib.auth.models import User
from celery import Celery, shared_task

LIMITS = {'cputime': 2, 'memory': 256}

EXECUTED = 0
TIME_LIMIT_EXCEEDED = 1
RUNTIME_ERROR = 2
COMPILATION_ERROR = 3
MEMORY_LIMIT_EXCEEDED = 4

PROFILES = []
for language in ProgrammingLanguage.objects.all():
    PROFILES.append(epicbox.Profile(
        language.name, language.dockerImage, None, 'root', False, True))
epicbox.configure(profiles=PROFILES)

# Create a celery queue for running tasks using epicbox
# app = Celery('judge', backend='rpc://', broker='pyamqp://guest@localhost//')


# This is to make sure that the task is completed before the next task is executed
@shared_task(acks_Late=True)
def evaluate(request, queueid):
    def execute(language: ProgrammingLanguage, codeFile, inputFile, outputFile):
        files = [{'name': codeFile.name,
                  'content': bytes(codeFile.read(), 'utf-8')}]
        if language.compileCommand != 'NA':
            toExecute = language.compileCommand.replace(
                'filename', codeFile.name)
            with epicbox.working_directory() as work_dir:
                result = epicbox.run(
                    language.name, toExecute, files=files, limits=LIMITS, workdir=work_dir)
                if result['exit_code'] != 0:
                    if result['timeout'] or result['oom_killed']:
                        outputFile.write(
                            "Error: Compilation exceeded time limit or memory limit")
                    else:
                        outputFile.write(result['stderr'].decode('utf-8'))
                    return COMPILATION_ERROR, result['duration']
                toExecute = "./a.out"
                result = epicbox.run(
                    language.name, toExecute, files=files, limits=LIMITS, stdin=inputFile.read(), workdir=work_dir)
                if result['timeout']:
                    outputFile.write("Time Limit Exceeded")
                    return TIME_LIMIT_EXCEEDED, result['duration']
                if result['oom_killed']:
                    outputFile.write("Memory Limit Exceeded")
                    return MEMORY_LIMIT_EXCEEDED, result['duration']
                if result['exit_code'] != 0:
                    outputFile.write(result['stderr'].decode('utf-8'))
                    return RUNTIME_ERROR, result['duration']
                outputFile.write(result['stdout'].decode('utf-8'))
                return EXECUTED, result['duration']
        if language.runCommand != 'NA':
            toExecute = language.executeCommand.replace(
                'filename', codeFile.name)
            result = epicbox.run(language.name, toExecute,
                                 files=files, stdin=inputFile.read(), limits=LIMITS)
            if result['timeout']:
                outputFile.write("Time Limit Exceeded")
                return TIME_LIMIT_EXCEEDED, result['duration']
            if result['oom_killed']:
                outputFile.write("Memory Limit Exceeded")
                return MEMORY_LIMIT_EXCEEDED, result['duration']
            if result['exit_code'] != 0:
                outputFile.write(result['stderr'].decode('utf-8'))
                return RUNTIME_ERROR, result['duration']
            outputFile.write(result['stdout'].decode('utf-8'))
            return EXECUTED, result['duration']
    newCodeRunner = CodeRunner.objects.get(queueNo=queueid)
    try:
        newCodeRunner.status = 'Running'
        newCodeRunner.save()
        problem = Problem.objects.get(pk=newCodeRunner.problem.problemId)
        testCase = TestCase.objects.filter(problem=problem)
        submission = Submission()
        submission.problem = problem
        submission.pub_date = datetime.datetime.now()
        submission.userCode = newCodeRunner.userCode
        submission.user = request.user
        for test in testCase.iterator():
            language = ProgrammingLanguage.objects.get(
                id=newCodeRunner.userLanguage)
            sol_file = open('./soln/code'+language.fileExtension, "w")
            sol_file.write(newCodeRunner.userCode)
            sol_file.close()
            inputFile = open('./soln/input.txt', "w")
            inputFile.write(test.expectedInput)
            inputFile.close()
            expectedOutputFile = open('./soln/output.txt', "w")
            expectedOutputFile.write(test.expectedOutput)
            expectedOutputFile.close()
            sol_file = open(sol_file.name, 'r')
            inputFile = open(inputFile.name, 'r')
            userOutputFile = open("./soln/out.txt", 'w')
            exitCode, cpuTime = execute(
                language, sol_file, inputFile, userOutputFile)
            sol_file.close()
            inputFile.close()
            expectedOutputFile.close()
            userOutputFile.close()
            if exitCode != EXECUTED:
                if exitCode == TIME_LIMIT_EXCEEDED:
                    submission.verdict = 'TIME LIMIT EXCEEDED'
                    submission.save()
                    newCodeRunner.status = 'COMPLETED'
                    newCodeRunner.save()
                    return render(request, 'judge/submissions.html', {'verdict': submission.verdict})
                elif exitCode == RUNTIME_ERROR:
                    submission.verdict = 'RUNTIME ERROR'
                    submission.save()
                    newCodeRunner.status = 'COMPLETED'
                    newCodeRunner.save()
                    return render(request, 'judge/submissions.html', {'verdict': submission.verdict})
                elif exitCode == COMPILATION_ERROR:
                    submission.verdict = 'Compilation Error'
                    submission.save()
                    newCodeRunner.status = 'COMPLETED'
                    newCodeRunner.save()
                    return render(request, 'judge/submissions.html', {'verdict': submission.verdict})
                elif exitCode == MEMORY_LIMIT_EXCEEDED:
                    submission.verdict = 'MEMORY LIMIT EXCEEDED'
                    submission.save()
                    newCodeRunner.status = 'COMPLETED'
                    newCodeRunner.save()
                    return render(request, 'judge/submissions.html', {'verdict': submission.verdict})
            else:
                if(filecmp.cmp('soln/output.txt', 'soln/out.txt', shallow=False)):
                    submission.verdict = "Accepted"
                else:
                    submission.verdict = "Wrong Answer"
                    submission.save()
                    newCodeRunner.status = 'COMPLETED'
                    newCodeRunner.save()
                    return render(request, 'judge/submissions.html', {'verdict': submission.verdict})
        submission.save()
        newCodeRunner.status = 'COMPLETED'
        newCodeRunner.save()
        problem.solveCount += 1
        problem.save()
        return render(request, 'judge/submissions.html', {'verdict': submission.verdict})
    except Exception as errorMessage:
        newCodeRunner.status = 'Failed'
        open('ErrorMessage.txt', 'w').write(str(errorMessage))
    newCodeRunner.save()
    return render(request, 'judge/submissions.html', {'verdict': 'Error'})
