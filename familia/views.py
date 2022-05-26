from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from familia.models import *
from familia.forms import PersonaForm



def index(request):
    personas = Persona.objects.all()
    return HttpResponse(render(request, "familia/index.html", {"personas":personas}))


def agregar(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            altura = form.cleaned_data['altura']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            email = form.cleaned_data['email']
            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, altura=altura).save()
            return HttpResponseRedirect("/familia/")
    
    elif request.method == "GET":
            form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")
    
    return render(request, "familia/form_carga.html", {"form":form})
            

def borrar(request, identificador):
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect("/familia/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")