from django.db import models
from apps.ordenes.models import Orden

class Envio(models.Model):
    ESTADOS = [
        ('Preparando', 'Preparando'),
        ('En camino', 'En camino'),
        ('Entregado', 'Entregado'),
    ]

    orden = models.OneToOneField(Orden, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Preparando')
    fecha_envio = models.DateTimeField(null=True, blank=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Envío de {self.orden} Se entrega el {self.fecha_envio}"
