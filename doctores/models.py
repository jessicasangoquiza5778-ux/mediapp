from django.db import models

class Doctor(models.Model):
    ESTADOS = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    nombre_doctor = models.CharField(max_length=100)
    apellido_doctor = models.CharField(max_length=100)
    cedula_doctor = models.CharField(max_length=10, unique=True)
    especialidad = models.CharField(max_length=100)
    telefono_doctor = models.CharField(max_length=15)
    correo_doctor = models.EmailField(blank=True)
    estado_doctor = models.CharField(max_length=20, choices=ESTADOS, default='activo')

    def __str__(self):
        return f"Dr(a). {self.nombre_doctor} {self.apellido_doctor} - {self.especialidad}"