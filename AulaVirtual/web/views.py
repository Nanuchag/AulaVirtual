from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

#funciones parametrizadas
def saludar(request, nombre):

    print(request.method)

    return HttpResponse(f'Bienvenid@ {nombre}')

def alumnos_por_año(request, year):
        alumnos = ["Jonathan", "Ellie", "Joel", "Dina"] # """"""""Levanta""""""" los usuarios de la BBDD
        return HttpResponse(f'listado de alumnos: {year} \n {alumnos}')