from sqlite3 import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.shortcuts import render, redirect
from gestorProductos.models import Producto
from gestorProductos.forms import ProductoForm
from django.urls import reverse



def productos_usuario(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'gestorUser/productosUsuario.html', {'productos': productos})

@login_required
def crear_producto_usuario(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)  # No guardes aún en la base de datos
            producto.creado_por = request.user  # Asigna el usuario autenticado
            try:
                producto.save()  # Guarda el producto en la base de datos
                return redirect('lista_productos_usuario')  # Cambia al nombre correcto de tu URL
            except IntegrityError as e:
                return render(request, 'error.html', {'error': e})  # Opcional, para manejar errores
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})


def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

# Vista para ver los usuarios
def ver_usuarios(request):
    usuarios = User.objects.all()  # Obtener todos los usuarios
    return render(request, 'registration/ver_usuarios.html', {'usuarios': usuarios})


def añadir_usuario(request):
    # Lógica para añadir un nuevo usuario
    return redirect(reverse('signup'))

def ver_productos(request):
    # Lógica para ver productos
    return render(request, 'gestorProductos/productosAdmin.html')

def añadir_producto(request):
    # Lógica para añadir un nuevo producto
    return render(request, 'gestorProductos/agregar_producto.html')

def ver_pedidos(request):
    # Lógica para ver pedidos
    return render(request, 'pedidos.html')

def añadir_pedido(request):
    # Lógica para añadir un nuevo pedido
    return render(request, 'añadir_pedido.html')

# Create your views here.
@login_required
def index(request):
    return render(request, "index.html")

def superuser_view(request):
    # verificar si el usuario es un superusuario
    if not request.user.is_superuser:
        return HttpResponseForbidden('No tienes permisos para ver esta pagina.')
    
    #logica especifica apra el superusuario
    return render(request, "superuser_dashboard.html",{
        'user': request.user
    })

# Vista para usuarios normales (con restricciones)
@login_required
def user_view(request):
    # Verificamos si el usuario es un superusuario
    if request.user.is_superuser:
        return HttpResponseForbidden("No tienes permisos para ver esta página.")
    
    # Lógica específica para los usuarios normales
    return render(request, 'user_dashboard.html', {
        'user': request.user
    })

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "¡Usuario creado exitosamente!"

