from django.shortcuts import render
from .logic import logic_user as ul
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
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
        print(form)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully created User')
            return HttpResponseRedirect(reverse('userPost'))
    return HttpResponse("Could not post")
