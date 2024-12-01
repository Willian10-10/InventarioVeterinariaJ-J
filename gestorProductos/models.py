from django.db import models

# modelo de los productos
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    precio = models.IntegerField()    
    stock = models.IntegerField()