from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registro_usuario(request):
    return render(request, 'registro_usuario.html')

def healthCheck(request):
    return HttpResponse('ok')