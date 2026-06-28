from django.db import models

class ComprobanteServicio(models.Model):
    numero_comprobante = models.CharField(max_length=50)
    fecha = models.DateField()
    cliente = models.CharField(max_length=100)
    descripcion = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.numero_comprobante