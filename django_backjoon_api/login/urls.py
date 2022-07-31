

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.get_problem, name='test'),
    path('backjoon/solved', views.getSolved, name='solved_test'),
]

