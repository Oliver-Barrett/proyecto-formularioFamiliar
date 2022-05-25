from django.http import HttpResponse
from django.shortcuts import render
from familia.models import *


def hola_mundo(request):
    return HttpResponse("Hola mundo")



def hola_soy_una_plantilla(request):
    oliver = Persona.objects.first()
    return HttpResponse(render(request, 'familia/index.html', {"about":oliver}))
