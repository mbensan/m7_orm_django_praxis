from django.contrib import admin

from libros.models import Libro


# Register your models here.
class LibroAdmin(admin.ModelAdmin):
  pass

admin.site.register(Libro, LibroAdmin)