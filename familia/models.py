from django.db import models


class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.CharField(max_length=100)
    altura = models.FloatField(default=0.0)
    fecha_nacimiento = models.DateField()
    email = models.TextField(max_length=100)


class Vehiculo(Persona):
    tipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.IntegerField()


class Celular(Vehiculo):
    marca_celular = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    numero = models.IntegerField()