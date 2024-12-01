from django.shortcuts import render
from .models import Producto

# Create your views here.
def inventarioAdmin(request):
    return render(request, 'gestorProductos/productosAdmin.html')
