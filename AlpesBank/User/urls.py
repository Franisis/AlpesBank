from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include
from . import views



urlpatterns =[
    url('^users/$', views.user),
    #url(r'^userCreate/', views.userPost , name = 'userPost'),
    path('user/<str:pk>/', views.user_detail, name='user-detail'),
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
]