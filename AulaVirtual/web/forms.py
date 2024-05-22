from django import forms

class AltaAlumnoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del alumno", required=True)
    apellido = forms.CharField(label="Apellido del alumno", required=True)
    dni = forms.IntegerField(label="DNI", required=True)
    email = forms.EmailField(label="email", required=True)