from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
# Create your views here.
def query1(req):
  # por la restricción de llave promaria, esta vista se puede ejecutar una sóla vez
  cursor = connection.cursor()
  cursor.execute("insert into main_curso (cod, nombre, activo) values ('RP4', 'Repostería', true)")
  return HttpResponse('listo')
