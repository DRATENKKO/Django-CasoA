from django.shortcuts import render
from .models import Tarjeta
# Create your views here.
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()

def listaTarjetas(request):
    tarjeta=Tarjeta.objects.all() #<=> SELECT * FROM Vehiculos
    #creo mi contexto para llevar los datos desde la tabla al html
    contexto={
        'Tarjetas': tarjeta
    }
    return render(request,'core/listaTarjetas.html',contexto)



def index(request):
    return render(request, 'core/index.html')

def Carrito(request):
    return render(request, 'core/Carrito.html')

def donacion(request):
    return render(request, 'core/donacion.html')

def Gato(request):
    return render(request, 'core/Gato.html')

def Perro(request):
    return render(request, 'core/Perro.html')

def tarjeta(request):
    return render(request, 'core/tarjeta.html')

def todos(request):
    return render(request, 'core/todos.html')

def test(request):
    lista=["lasaña","Charquican","Porotos verdes"]
    hijo=Persona("JUANITO","10")
    contexto={"nombre":"anita la huerfanita","comidas": lista, "hijo":hijo}
    return render(request, 'core/test.html',contexto)
