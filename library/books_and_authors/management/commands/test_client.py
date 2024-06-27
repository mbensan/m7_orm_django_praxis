from django.core.management.base import BaseCommand
from books_and_authors.models import Client

# se ejecuta: python manage.py test_client

class Command(BaseCommand):

  def handle (self, *args, **kwargs):
    # probamos que se pueda agregar un nuevo Cliente
    c = Client(first_name="Fernando", last_name='Jara', email='fjrara@gmail.com',
          height=1.76)
    c.save()
    print('Cliente creado')



