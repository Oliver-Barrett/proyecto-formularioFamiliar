from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    altura = forms.FloatField(label="Altura")
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento", input_formats=["%d/%m/%Y"],
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    email = forms.EmailField(label="Email")
    tipo = forms.CharField(label="Tipo de vehiculo", max_length=100)
    marca = forms.CharField(label="Marca del vehiculo", max_length=100)
    modelo = forms.IntegerField(label="Modelo del vehiculo",max_value=3000)
    marca_celular = forms.CharField(label="Marca de celular", max_length=100)
    empresa = forms.CharField(label="Empresa",max_length=100)
    numero = forms.IntegerField(label="Numero de celular", max_value=9999999999)


class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")