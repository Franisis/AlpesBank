from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns =[
    path('users/', views.userGet, name = 'userGet'),
    path('userCreate/', views.userPost, name = 'userPost'),
]