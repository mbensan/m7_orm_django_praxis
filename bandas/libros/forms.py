from django import forms
from django.forms import ModelForm
from libros.models import Libro

class LibroModelForm(ModelForm):
  class Meta:
    model = Libro
    fields = ['titulo', 'autor', 'fecha_publicacion']
    widgets = {
      'titulo': forms.TextInput(
        attrs = {
          'class': 'form-control'
        }
      ),
      'autor': forms.TextInput(
        attrs = {
          'class': 'form-control'
        }
      ),
      'fecha_publicacion': forms.DateInput(
        attrs = {
          'class': 'form-control'
        }
      ),
    }
