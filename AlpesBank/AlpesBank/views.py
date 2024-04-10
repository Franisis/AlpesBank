from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registro_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        return HttpResponse(nombre+' ¡Su usuario fue registrado exitosamente!')
    else:
        return render(request, 'registro_usuario.html')

def healthCheck(request):
    return HttpResponse('ok')