import json
from urllib import response
import urllib.request
import requests 
from django.shortcuts import render
from django.http import HttpResponse
import rest_framework 
from .models import Problem
# Create your tests here.

def get_problem(request):
    if 'name' in request.GET:
        name = request.GET['name']
        print(name)
        url = "https://solved.ac/api/v3/user/problem_stats?handle=%s" % name

        print(url)
        response = requests.get(url)
        data = response.json() # json 형태로 변환
        print(data)
        for i in data:
            problem_data = Problem(
                level = i['level'],
            )
            problem_data.save()
    return render(request, 'problem.html' )
    #return HttpResponse("result_list")
    

def test(request):
    url = "https://solved.ac/api/v3/user/problem_stats"
    params = {"handle": "jjongyn"}
    result = requests.get(url, params=params)
    print(result)
    #result = requests.get(url)
    result_list = result.json()
    print(result_list)
    return HttpResponse("result_list")
