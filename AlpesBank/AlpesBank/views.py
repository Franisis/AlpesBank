from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from AlpesBank.auth0backend import getRole
from User.forms import UserForm


def index(request):
    return render(request, 'index.html')

def registro_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        respuesta = requests.get('http://35.188.169.4:8080/usercrm/')
        mensaje = respuesta.json()['mensaje']
        #return JsonResponse({'mensaje': mensaje})
        if mensaje == '1':
            return render(request, 'registro_exitoso.html')
        else:
            return render(request, 'registro_fallido.html')
    else:
        return render(request, 'registro_usuario.html')

def formulario_cliente(request):
    if request.method == 'POST':
        formulario = UserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        # Procesar el formulario si es necesario
            return render(request, 'formulario_cliente.html')
    else:
        render(request, 'formulario_cliente.html')
    if request.method == 'GET':
        respuesta = requests.get('http://35.188.169.4:8080/usercrm/')
        mensaje = respuesta.json()['mensaje']
        return JsonResponse({'mensaje': mensaje})

    return JsonResponse({'mensaje': 'Método no permitido'})

def healthCheck(request):
    return HttpResponse('ok')