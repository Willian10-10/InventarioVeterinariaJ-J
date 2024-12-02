from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Producto, Categoria
from .forms import ProductoForm

# Create your views here.
from .models import Producto

def inventarioAdmin(request):
    productos = Producto.objects.all()
    return render(request, 'gestorProductos/productosAdmin.html', {'productos': productos})


def lista_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'productos.html', {'productos': productos, 'categorias': categorias})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productosAdmin') 
    else:
        form = ProductoForm()
    
    return render(request, 'gestorProductos/agregar_producto.html', {'form': form})

# Vista para eliminar un producto
def eliminar_producto(request, producto_id):
    # Obtener el producto a eliminar
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Eliminar el producto
    producto.delete()
    
    # Redirigir al listado de productos
    return redirect('productosAdmin')
    
# Vista para editar un producto
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    form = ProductoForm(instance = producto)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productosAdmin') 
    else:
        form = ProductoForm()
    
    return render(request, 'gestorProductos/agregar_producto.html', {'form': form})


#vista para mostrar los productos generados en la pagina principal
def index(request):
    productos = Producto.objects.all()  
    return render(request, 'index.html', {'productos': productos})

#redirgir vista segun usuario
def gestionar_productos(request):
    if request.user.is_superuser:
        return redirect('productosAdmin')  # Ruta definida en las URLs para superusuario
    elif request.user.is_authenticated:
        return redirect('productosUsuario')  # Ruta definida en las URLs para usuario normal
    else:
        return redirect('login')  # Si no está autenticado, redirigir al login


""" def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        categoria_id = request.POST.get('categoria')

        # Validación y guardado
        if categoria_id:
            producto.categoria = get_object_or_404(Categoria, id=categoria_id)
            producto.save()
            return redirect('lista_productos')

    categorias = Categoria.objects.all()
    return render(request, 'editar_producto.html', {'producto': producto, 'categorias': categorias}) """



# Vista para agregar una categoría
""" def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')

        if nombre:
            Categoria.objects.create(nombre=nombre, descripcion=descripcion)
            return redirect('lista_productos')

    return render(request, 'agregar_categoria.html')

# Vista para eliminar una categoría
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_productos')
    return render(request, 'confirmar_eliminacion_categoria.html', {'categoria': categoria})
 """