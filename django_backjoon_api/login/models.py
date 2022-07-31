from django.db import models

class Problem(models.Model):
    level = models.CharField(max_length=50, blank = True, null = True)
    

    def __str__(self):
        return self.level

class solvedProblem(models.Model):
    problem_ID = models.CharField(max_length=30)
