from django.db import models

class Platillo(models.Model):
    CATEGORIA_CHOICES = [
        ('bebida', 'Bebida'),
        ('comida', 'Comida'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return self.nombre
