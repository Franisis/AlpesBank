from django.http import HttpResponse
from django.shortcuts import render


def healthCheck(request):
    return HttpResponse('ok')