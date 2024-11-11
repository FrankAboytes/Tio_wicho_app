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

class ClienteSession(models.Model):
    mesa_id = models.CharField(max_length=50, unique=True)  # Identificación de la mesa
    estado = models.BooleanField(default=True)  # True si la sesión está abierta, False si está cerrada
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la sesión

    def __str__(self):
        return f"Mesa {self.mesa_id} - {'Abierta' if self.estado else 'Cerrada'}"

class Mesa(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    nombre_platillo = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    es_bebida = models.BooleanField(default=False)  # True si es una bebida, False si es comida
    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default="pendiente")  # pendiente, en preparación, listo

    def subtotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        return f"{self.nombre_platillo} - Cantidad: {self.cantidad} - Mesa: {self.mesa.nombre}"

class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)
    categoria = models.CharField(max_length=100, default="Bebida")

    def __str__(self):
        return self.nombre
