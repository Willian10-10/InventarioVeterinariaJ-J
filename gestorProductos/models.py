from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)  # Texto breve

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)  # Texto breve
    precio = models.CharField(max_length=50)  # Representar números como texto
    categoria = models.CharField(max_length=100)  # Sin relación, solo texto

    def __str__(self):
        return self.nombre