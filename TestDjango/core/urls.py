from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('donacion.html', views.donacion, name='donacion'),
    path('Carrito.html', views.Carrito, name='Carrito'),
    path('Gato.html', views.Gato, name='Gato'),
    path('Perro.html', views.Perro, name='Perro'),
    path('tarjeta.html', views.tarjeta, name='tarjeta'),
    path('todos.html', views.todos, name='todos'),
    path('listaTarjetas.html', views.listaTarjetas, name='listaTarjetas'),
    path('form_tarjeta.html', views.form_tarjeta, name='form_tarjeta'),
]

