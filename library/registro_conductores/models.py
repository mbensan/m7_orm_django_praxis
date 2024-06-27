from django.db import models
from django.utils import timezone

# Create your models here.
def mayor18(value):
  pass

class Conductor(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  fecha_nac = models.DateField(validators=[mayor18]) # Validar que sea mayor a 18 años

  def __str__(self):
    return f'{self.nombre} {self.apellido}'

class Direccion(models.Model):
  regiones = (
    ('iii', 'Atacama'),
    ('v', 'Valparaíso'),
    ('ix', 'Araucanía'),
    ('vi', "O'higgins")
  )
  calle = models.CharField(max_length=50)
  numero = models.CharField(max_length=10)
  comuna = models.CharField(max_length=50)
  region = models.CharField(max_length=50, choices=regiones)
  conductor = models.OneToOneField(Conductor, related_name='direccion', on_delete=models.CASCADE)
  # conductor_id

  def __str__(self):
    return f'{self.calle} {self.numero}, {self.comuna}'

class Vehiculo(models.Model):
  patente = models.CharField(max_length=10)
  marca = models.CharField(max_length=50)
  modelo = models.CharField(max_length=50)
  año = models.DateField(default=timezone.now)
  conductor = models.ForeignKey(Conductor, related_name='vehiculos', on_delete=models.CASCADE)