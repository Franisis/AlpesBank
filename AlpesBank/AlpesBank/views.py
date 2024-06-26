from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from AlpesBank.auth0backend import getRole
from User.forms import UserForm
from User import views
from User.logic import logic_user as logic
from rest_framework.parsers import JSONParser
import requests

def index(request):
    return render(request, 'index.html')

def registro_usuario(request):
    if request.method == 'POST':
        info = {
        "id": request.POST['id'],
        "nombre": request.POST['name'],
        "apellido": request.POST['lastname'],
        "cedula": request.POST['cedula'],
        "correo": request.POST['correo'],
        "telefono": request.POST['telefono'],
        }
        respuesta = requests.post('http://35.188.169.4:8080/user/', json=info)
        print(respuesta.json())
        mensaje = respuesta.json().get('msg', 'Mensaje no encontrado')
        
        if mensaje == '1':
            logic.createUser(request.POST)
            return render(request, 'registro_exitoso.html')
        else:
            return render(request, 'registro_fallido.html')
    else:
        return render(request, 'registro_usuario.html')


# def registro_usuario(nombre, apellido, cedula, correo, telefono):
#     url = "http://35.188.169.4:8080/user/"
#     payload = {
#         "nombre": nombre,
#         "apellido": apellido,
#         "cedula": cedula,
#         "correo": correo,
#         "telefono": telefono
#     }
#     response = requests.post(url, json=payload)
#     if response == '1':
#             logic.createUser(response.POST)
#             return render(response, 'registro_exitoso.html')
#     else:
#             return render(response, 'registro_fallido.html')
    #return response.json()


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