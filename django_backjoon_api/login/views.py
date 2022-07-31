import json
from urllib import response
import urllib.request
import requests 
from django.shortcuts import render
from django.http import HttpResponse
import rest_framework 
from .models import Problem, solvedProblem
# Create your tests here.

def getSolved(request):
    all_solvedProbled = {}
    if 'user_id' in request.GET:
        user_id = request.GET['user_id']
        print(user_id)
        url = "https://solved.ac/api/v3/search/problem?query=solved_by%3A{}&sort=level&direction=desc" .format(user_id)
        print(url)
        get_url = requests.get(url)
        
        if get_url.status_code == requests.codes.ok:
            solved = json.loads(get_url.content.decode('utf-8'))
            
            #user_solved_cnt = solved.get("count")
            user_solved_items = solved.get("items")
            #print(user_solved_cnt)
            print(user_solved_items[0]) # 값이 이상하게 2개의 list로 들어옴
            #solved_list = []
            # 일단 푼 문제 리스트만 받아오기. 나중에 DB에 있는 값과 비교 해야겠지?
            for item in user_solved_items:
                print(item)
                solved_data = solvedProblem(
                    problem_ID = item['problemId'],
                )
                solved_data.save()
            all_solvedProbled = solvedProblem.objects.all().order_by('-id')
        else:
            print("error")
    #context = {'solved_list : ': solved_list}
    return render(request, 'problem.html', {'all_solvedProbled':all_solvedProbled})


def get_problem(request):
    if 'name' in request.GET:
        name = request.GET['name']
        # print(name)
        url = "https://solved.ac/api/v3/user/problem_stats?handle=%s" % name
        # print(url)
        response = requests.get(url)
        data = response.json() # json 형태로 변환
        # print(data)
        for i in data:
            problem_data = Problem(
                level = i['level'],
            )
            problem_data.save()
    return render(request, 'problem.html' )

            
        

    

def test(request):
    url = "https://solved.ac/api/v3/user/problem_stats"
    params = {"handle": "jjongyn"}
    result = requests.get(url, params=params)
    print(result)
    #result = requests.get(url)
    result_list = result.json()
    print(result_list)
    return HttpResponse("result_list")
