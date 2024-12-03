from django.urls import path, include

from gestorUser.views import SignUpView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('superuser-dashboard/', views.superuser_view, name='superuser_dashboard'),
    path('ver-usuarios/', views.ver_usuarios, name='ver_usuarios'),
    path('añadir-usuario/', views.añadir_usuario, name='añadir_usuario'),
    path('ver_productos/', views.ver_productos, name='ver_productos'),
    path('añadir_producto/', views.añadir_producto, name='añadir_producto'),
    path('ver_pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('añadir_pedido/', views.añadir_pedido, name='añadir_pedido'),
    path('sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
]