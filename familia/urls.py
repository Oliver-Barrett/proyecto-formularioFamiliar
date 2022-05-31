from familia.views import *
from django.urls import path



urlpatterns = [
    path("", index, name="index"),
    path("agregar/", agregar, name="agregar"),
    path("borrar/<identificador>", borrar, name="borrar"),
    path("buscar/", buscar, name="buscar"),
]