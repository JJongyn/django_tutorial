import imp
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Accounts
from .serializers import AccountsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(['GET'])
def getAccounts(request):
    data = Accounts.objects.all()
    serializer = AccountsSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAccountsDetail(request, pk):
    data = Accounts.objects.get(pk=pk)
    serializer = AccountsSerializer(data, many=True)
    return Response(serializer.data)
    

@api_view(['POST'])
def registerAccount(request):
    data = JSONParser().parse(request)
    serializer = AccountsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    else:
        return JsonResponse(serializer.errors, status=400)
    
    return redirect('registration:getAccounts')