from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.CharField(max_length=20)
    totalScore = models.FloatField(default=0)

class Problem(models.Model):
    problemId=models.IntegerField()
    problemText = models.TextField()
    difficulty=models.CharField(max_length=15)
    status=models.CharField(max_length=15)#Solved/Unsolved
    score=models.FloatField()



class TestCase(models.Model):
    problems = models.ForeignKey(Problem, on_delete=models.CASCADE)
    expectedInput = models.TextField()
    expectedOutput = models.TextField()


class Submission(models.Model):
    problems = models.ForeignKey(Problem, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    verdict=models.CharField(max_length=15)
  
