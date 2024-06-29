from django.db import models

# Create your models here.
class Estudiante(models.Model):
  rut = models.CharField(max_length=9, primary_key=True)
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  fecha_nac = models.DateField()
  activo = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  # cursos

class Profesor(models.Model):
  rut = models.CharField(max_length=9, primary_key=True)
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  activo = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  # cursos

class Curso(models.Model):
  codigo = models.CharField(max_length=10, primary_key=True)
  nombre = models.CharField(max_length=50)
  version = models.IntegerField()
  profesor = models.ForeignKey(
    Profesor, 
    related_name='cursos', 
    null=True, 
    on_delete=models.CASCADE)
  estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')
