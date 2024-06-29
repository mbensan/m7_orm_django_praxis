from django.shortcuts import render, HttpResponse
from institucion.services import crear_curso,\
  crear_estudiante, agregar_curso_a_estudiante\
  , crear_profesor, agregar_profesor_a_curso

# Create your views here.
def test(req):
  # crear_curso('CLO', 'Complete Loración', 1)
  # crear_estudiante('1234567-8', 'Tutu Tutu', 'Cajarito', '2000-03-05')
  #agregar_curso_a_estudiante('CLO', '1234567-8')
  # crear_profesor('654321-1', 'Profesor', 'Salomón')
  agregar_profesor_a_curso('654321-1', 'CLO')
  return HttpResponse('OK')

