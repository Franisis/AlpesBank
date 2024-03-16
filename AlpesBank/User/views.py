from django.shortcuts import render
from .logic import logic_user as ul
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from .forms import UserForm



# Create your views here.

def userGet(request):
    if request.method=="GET":
        users = ul.get_users()
        users_dto = serializers.serialize('json', users)
        return HttpResponse(users_dto, 'application/json')

def userPost(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            ul.create_user(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created User')
            return HttpResponseRedirect(reverse('userPost'))
    else:
        form = UserForm()

    context = {
        'form': form,
    }
    return HttpResponse(context)    

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
    return render(request, 'user_detail.html', {'user': user})
        
    


