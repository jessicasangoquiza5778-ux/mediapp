from django.db import models
from django.conf import settings


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="paciente")
    documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.documento


class Medico(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="medico")
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True, related_name="medicos")
    licencia = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.licencia


class Cita(models.Model):
    ESTADO_CHOICES = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("realizada", "Realizada"),
        ("cancelada", "Cancelada"),
    ]
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="citas")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="citas")
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default="pendiente")
    motivo = models.TextField(blank=True)
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cita {self.id}"


class HistorialMedico(models.Model):
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE, related_name="historial")
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="historiales")
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True, blank=True, related_name="historiales_realizados")
    diagnostico = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Historial {self.id}"


class Receta(models.Model):
    historial = models.ForeignKey(HistorialMedico, on_delete=models.CASCADE, related_name="recetas")
    medicamentos = models.TextField()
    indicaciones = models.TextField(blank=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receta {self.id}"
