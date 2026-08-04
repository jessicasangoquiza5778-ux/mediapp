from django.db import models

# Create your models here.

class Pacientes(models.Model):
    nombre_Pacientes = models.CharField(max_length=100)
    apellido_Pacientes = models.CharField(max_length=100)
    cedula_Pacientes = models.CharField(max_length=10)
    telefono_Pacientes = models.CharField(max_length=15)
    direccion_Pacientes = models.CharField(max_length=255)
    estado_Pacientes = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre_Pacientes} {self.apellido_Pacientes}"