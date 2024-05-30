from django.shortcuts import render
from .logic import logic_user as ul
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from .forms import UserForm

#import requests
from django.shortcuts import render
from django.http import JsonResponse
from AlpesBank.auth0backend import getRole
from django.contrib.auth.decorators import login_required
#Sprint 4
from bson.objectid import ObjectId
from pymongo import MongoClient
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
# Create your views here.


def userGet(request):
    if request.method == "GET":
        users = ul.get_users()
        user_dicts = [user.__dict__ for user in users]  # Convert each user object to a dictionary
        return JsonResponse(user_dicts, safe=False) 

@api_view(["POST"])
def userPost(request):
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
            user = ul.createUser(data)
            response = {
                "objectId": str(user.id),
                "message": f"User {user.name} created in DB"
            }
            return JsonResponse(response, safe=False)
        except ValueError as e:
            print(request)
            return JsonResponse({"error":str(e)}, status=400)
    
   
@login_required
def user_detail(request, pk):
    role = getRole(request)
    if role == "asesor":
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
    else:
        return render(request, 'acceso_denegado.html')
    


