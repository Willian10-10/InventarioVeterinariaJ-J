from django.db import models
# from gestorUser.models import CustomUser  

<<<<<<< HEAD
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
   # creador = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
=======
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
>>>>>>> ca89f90409cb29469cfc783817dfce9d0b2e1888

    def __str__(self):
        return self.nombre
