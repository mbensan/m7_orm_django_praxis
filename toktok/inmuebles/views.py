from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from main.models import Inmueble, Region, Comuna

# vamos a crear un test que sólo pasan los 'arrendadores'
def solo_arrendadores(user):
  if user.user_profile.rol == 'arrendador' or user.is_staff == True:
    return True
  else:
    return False

@user_passes_test(solo_arrendadores)
def nuevo_inmueble(req):
  # nos traemos la información de las comunas y las regiones
  regiones = Region.objects.all()
  comunas = Comuna.objects.all()
  # pasar los datos requeridos por el formulario
  context = {
    'tipos_inmueble': Inmueble.tipos,
    'regiones': regiones,
    'comunas': comunas
  }
  return render(req, 'nuevo_inmueble.html', context)
