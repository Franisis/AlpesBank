from django.shortcuts import render
from .logic import logic_user as ul
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from .forms import UserForm

import requests
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.






def userGet(request):
    if request.method=="GET":
        users = ul.get_users()
        users_dto = serializers.serialize('json', users)
        return HttpResponse(users_dto, 'application/json')

def userPost(request):
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        respuesta = requests.get('http://35.188.169.4:8080/usercrm/')
        mensaje = respuesta.json()['mensaje']
        #return JsonResponse({'mensaje': mensaje})
        if mensaje == '1':
            return render(request, 'registro_exitoso.html')
        else:
            return render(request, 'registro_fallido.html')
      

def user_detail(request, pk):
    
    # Intenta obtener el usuario por su clave primaria (id)
    user = ul.get_by_id(pk)
    
    # Aquí puedes hacer lo que quieras con el objeto de usuario
    user_data = {
        'name': user.name,
        'lastName': user.lastName,
        'cedula': user.cedula,
        'correo': user.correo,
        'telefono': user.telefono,
        #'document': user.document
    }

    # Devuelve los datos del usuario como una respuesta JSON
    return render(request, 'user.html', {'user': user})
        
    


