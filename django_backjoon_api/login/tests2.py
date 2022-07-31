import json
from urllib import response
import urllib.request
import requests
from django.shortcuts import render
from django.http import HttpResponse
import rest_framework 
# Create your tests here.

def test(request):
    url = "https://solved.ac/api/v3/user/problem_stats?handle=jjongyn"
    '''
    header = {
    "Content-Type":"application/json",
    "handle":"jjongyn",
    }
    '''
    
    result = requests.get(url)
    result_list = result.json()
    print(result_list)
    return HttpResponse("result_list")
    #if result.status_code == 200:
    #    return HttpResponse('Successful')
    #return HttpResponse('Something went wrong')