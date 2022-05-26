from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    altura = forms.FloatField(label="Altura")
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento", input_formats=["%d/%m/%Y"],
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    email = forms.EmailField(label="Email")