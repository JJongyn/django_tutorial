from django.contrib import admin
from .models import Problem, solvedProblem
# Register your models here.
admin.site.register(Problem)
admin.site.register(solvedProblem)