from django.db import models


class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.CharField(max_length=100)
    altura = models.FloatField()
    fecha_nacimiento = models.DateField()
    email = models.TextField(max_length=100)
