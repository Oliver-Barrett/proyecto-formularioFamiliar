
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
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
            
            return HttpResponseRedirect(reverse("index"))
    
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
        return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def buscar(request):
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarPersonasForm(request.GET)
        if form_busqueda.is_valid():
            personas = Persona.objects.filter(nombre__icontains=request.GET.get("palabra_a_buscar"))
            return render(request, "familia/lista_familiares.html", {"personas":personas, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarPersonasForm()
        return render(request, "familia/form_busqueda.html", {"form_busqueda":form_busqueda})


def actualizar(request, identificador=''):
   
    if request.method == "GET":
        persona = get_object_or_404(Celular, pk=int(identificador))
        initial = {
            "id": persona.id,
            "nombre": persona.nombre, 
            "apellido": persona.apellido,
            "altura": persona.altura,
            "fecha_nacimiento": persona.fecha_nacimiento.strftime("%d/%m/%Y"),
            "email": persona.email,
            "tipo": persona.tipo,
            "marca": persona.marca,
            "modelo": persona.modelo,
            "marca_celular": persona.marca_celular,
            "empresa": persona.empresa,
            "numero": persona.numero,
        }
    
        form_actualizar = ActualizarPersonaForm(initial=initial)
        return render(request, 'familia/form_carga.html', {'form': form_actualizar, 'actualizar': True})
    
    elif request.method == "POST":
        form_actualizar = ActualizarPersonaForm(request.POST)
        if form_actualizar.is_valid():
            persona = get_object_or_404(Celular, pk=form_actualizar.cleaned_data['id'])
            persona.nombre = form_actualizar.cleaned_data['nombre']
            persona.apellido = form_actualizar.cleaned_data['apellido']
            persona.altura = form_actualizar.cleaned_data['altura']
            persona.fecha_nacimiento = form_actualizar.cleaned_data['fecha_nacimiento']
            persona.email = form_actualizar.cleaned_data['email']
            persona.tipo = form_actualizar.cleaned_data['tipo']
            persona.marca = form_actualizar.cleaned_data['marca']
            persona.modelo = form_actualizar.cleaned_data['modelo']
            persona.marca_celular = form_actualizar.cleaned_data['marca_celular']
            persona.empresa = form_actualizar.cleaned_data['empresa']
            persona.numero = form_actualizar.cleaned_data['numero']
            persona.save()

            return HttpResponseRedirect(reverse("index"))

    