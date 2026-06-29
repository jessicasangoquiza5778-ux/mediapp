from django.db import models

# Create your models here.
from django.db import models

class Vehiculo(models.Model):
    placa_vehiculo = models.CharField(max_length=20)
    marca_vehiculo = models.CharField(max_length=50)
    modelo_vehiculo = models.CharField(max_length=50)
    anio_vehiculo = models.IntegerField()
    color_vehiculo = models.CharField(max_length=30)
    tipo_vehiculo = models.CharField(max_length=30)
    estado_vehiculo = models.CharField(max_length=20)

    def __str__(self):
        return self.placa_vehiculo