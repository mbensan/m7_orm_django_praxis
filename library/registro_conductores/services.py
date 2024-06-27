from registro_conductores.models import Conductor, Direccion, Vehiculo

def crear_conductor(nombre, apellido, fecha_nac):
  conductor = Conductor(nombre = nombre, apellido = apellido, fecha_nac = fecha_nac)
  conductor.save()
  imprimir_modelos()

def agregar_direccion(calle, numero, comuna, region, conductor_id):
  d = Direccion(calle=calle, numero=numero, region=region, comuna=comuna, conductor_id=conductor_id)
  d.save()
  imprimir_modelos()

def imprimir_modelos():
  conductores = Conductor.objects.all()
  direcciones = Direccion.objects.all()
  print(conductores)
  print(direcciones)
