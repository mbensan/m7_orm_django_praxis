from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from libros.models import Libro
from libros.forms import LibroModelForm

# Create your views here.
def mostrar_libros (req):
  # 1. COnsultar libros en la base de datos
  libros = Libro.objects.all()
  # 2. Creo el diccionario context
  context = {
    'libros': libros
  }
  # 3. Cargo el template
  return render(req, 'libros.html', context)

# funcion multifuncional
def agregar_libro (req):
  if req.method == 'GET':
    form = LibroModelForm()
    context = {
      'form': form
    }
    return render(req, 'nuevo_libro.html', context)
  else: # req.method == POST
    # 1. Creamos un ModelForm a partir de los datos del formulario HTML
    form = LibroModelForm(req.POST)
    # 2. Lo guardamos
    new_libro = form.save()
    # 3. Le damos feedback al usuario
    messages.success(req, 'Buena! Haz creado un libro')
    return redirect('/libros/')