from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pointsEarned = models.FloatField(default=0)
    solved = ArrayField(ArrayField(models.IntegerField()))


class Problem(models.Model):
    problemId = models.AutoField(primary_key=True)
    problemName = models.CharField(max_length=100)
    problemText = models.TextField()
    difficulty = models.CharField(max_length=15)
    solveCount = models.IntegerField()
    score = models.FloatField()
    editorial = models.URLField(blank=True, null=True)


class TestCase(models.Model):
    problem = models.ForeignKey(
        Problem, related_name='testcases', on_delete=models.CASCADE)
    expectedInput = models.TextField()
    expectedOutput = models.TextField()


class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    id = models.AutoField(unique=True, primary_key=True, null=False)
    pub_date = models.DateTimeField('date published')
    userCode = models.TextField()
    verdict = models.CharField(max_length=50)
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    cpuTime = models.FloatField(default=0)


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=255)
    id = models.AutoField(unique=True, primary_key=True, null=False)
    compileCommand = models.TextField(null=True)
    executeCommand = models.TextField(null=True)
    dockerImage = models.TextField(null=True)
    fileExtension = models.CharField(default='.cpp', max_length=255)


class CodeRunner(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    userCode = models.TextField()
    userLanguage = models.IntegerField()
    queueNo = models.AutoField(primary_key=True)
    pub_date = models.DateTimeField('date published')
