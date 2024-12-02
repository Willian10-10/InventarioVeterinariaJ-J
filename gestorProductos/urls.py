from django.shortcuts import render
from .models import Producto
from django.urls import path
from . import views

def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

urlpatterns = [
    path('', views.index, name='index'),  # Redirección según usuario
    path('productos/', views.productos_admin, name='productosAdmin'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    
]