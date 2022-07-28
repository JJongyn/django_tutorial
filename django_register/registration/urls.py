from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from .views import getAccounts, getAccountsDetail

urlpatterns = [
    path('account/', getAccounts),
    path('account/<int:pk>', getAccountsDetail),
 
]
