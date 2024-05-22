from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import datetime
from .forms import *

# Create your views here.

def index(request):

    # Accedo a la BBDD a traves de los modelos
    context = {
         'nombre': 'Carlos',
         'fecha_hora': datetime.datetime.now()
    }
    return render(request, 'web/index.html', context)

#funciones parametrizadas
def saludar(request, nombre):

    print(request.method)

    return HttpResponse(f'Bienvenid@ {nombre}')

def alumnos_por_año(request, year):
        alumnos = ["Jonathan", "Ellie", "Joel", "Dina"] # """"""""Levanta""""""" los usuarios de la BBDD
        return HttpResponse(f'listado de alumnos: {year} \n {alumnos}')


def listado_alumnos(request):
     #estruturas cíclicas con templates
     context = {
          'alumnos': [
               'Carlos Lopez',
               'Maria Del Cerro',
               'Gaston Perez'
          ],
          'cuota_al_dia': True
     }
      

     return render(request, 'web/listado_alumnos.html', context)

def alta_alumno(request):

     context = {}

     if request.method == "GET":
          context['alta_alumno_form'] = AltaAlumnoForm()
     
     else: # Asumo que es un POST 
          context['alta_alumno_form'] = AltaAlumnoForm(request.POST)

          # Validar el form

          # Si el form es correcto
          # Lo redirijo a una vista segura, for exemple el index

          # Si el form es incorrecto
          # Renderizo un form con mensajes de error

          print(request.POST)

          return redirect('index')
     
     return render(request, 'web/alta_alumno.html', context)