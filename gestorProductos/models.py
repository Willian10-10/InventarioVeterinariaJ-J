from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    precio = models.IntegerField()    
    stock = models.IntegerField()