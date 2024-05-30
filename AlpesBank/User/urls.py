from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include
from . import views



urlpatterns =[
    path('users/', views.userGet, name = 'userGet'),
    path(r'userCreate/', views.userPost , name = 'userPost'),
    path('user/<int:pk>/', views.user_detail, name='user-detail'),
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
]