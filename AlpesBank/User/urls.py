from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns =[
    path('users/', views.userGet, name = 'userGet'),
    path('registro/', csrf_exempt(views.userPost), name = 'userPost'),
    path('user/<int:pk>/', views.user_detail, name='user-detail'),
]