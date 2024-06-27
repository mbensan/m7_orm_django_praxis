# Generated by Django 5.0.6 on 2024-06-26 23:30

import django.db.models.deletion
import django.utils.timezone
import registro_conductores.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField(validators=[registro_conductores.models.mayor18])),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('comuna', models.CharField(max_length=50)),
                ('region', models.CharField(choices=[('iii', 'Atacama'), ('v', 'Valparaíso'), ('ix', 'Araucanía'), ('vi', "O'higgins")], max_length=50)),
                ('conductor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='direccion', to='registro_conductores.conductor')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('año', models.DateField(default=django.utils.timezone.now)),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehiculos', to='registro_conductores.conductor')),
            ],
        ),
    ]
