from institucion.models import Curso, Estudiante, Profesor

def crear_curso(codigo, nombre, version):
  c = Curso(version=version, codigo=codigo, nombre=nombre)
  c.save()

def crear_estudiante(rut, nombre, apellido, fecha_nac):
  e = Estudiante(rut=rut,
                 nombre=nombre,
                 apellido=apellido,
                 fecha_nac=fecha_nac,
                 activo=True)
  e.save()

def crear_profesor(rut, nombre, apellido):
  p = Profesor(rut=rut,
               nombre=nombre,
               apellido=apellido,
               activo=True)
  p.save()

def agregar_curso_a_estudiante(curso_codigo, estudiante_rut):
  # ce = CursoEstudiante(curso_codigo=curso_codigo, estudiante_rut=estudiante_rut)
  # ce.save()
  # 1. Recuperamos el curso y el estudiante que deseamos vincular
  c = Curso.objects.get(codigo=curso_codigo)
  e = Estudiante.objects.get(rut=estudiante_rut)
  # 2. Viculamos ambas entidades
  c.estudiantes.add(e)

def agregar_profesor_a_curso(profesor_rut, curso_codigo):
  # 1. Me traigo ambas entidades
  p = Profesor.objects.get(rut=profesor_rut)
  c = Curso.objects.get(codigo=curso_codigo)
  # 2. Las vinculo
  c.profesor = p
  c.save()


def saludar(tercera, primera, segunda):
  print('hola ' + primera)
  print('hola ' + segunda)
  print('hola ' + tercera)



def promedio(a, b, c, num):
  return (a+b+c)/num

