from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from familia.models import *
from familia.forms import *



def index(request):
    personas = Celular.objects.all()
    return HttpResponse(render(request, "familia/lista_familiares.html", {"personas":personas}))


def agregar(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            altura = form.cleaned_data['altura']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            email = form.cleaned_data['email']
            tipo = form.cleaned_data['tipo']
            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            marca_celular = form.cleaned_data['marca_celular']
            empresa = form.cleaned_data['empresa']
            numero = form.cleaned_data['numero']

            Persona, Vehiculo, Celular(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, altura=altura, tipo=tipo, marca=marca, modelo=modelo, marca_celular=marca_celular, empresa=empresa, numero=numero).save()
            
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


def buscar(request):
    if request.method == "GET":
        form_busqueda = BuscarPersonasForm()

        return render(request, "familia/form_busqueda.html", {"form_busqueda":form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarPersonasForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            personas = Persona.objects.filter(nombre__icontains=palabra_a_buscar)

    return render(request, "familia/lista_familiares.html", {"personas":personas})