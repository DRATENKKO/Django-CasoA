from django.shortcuts import render, redirect
from .models import Tarjeta
from django. views. decorators.csrf import csrf_exempt
from core.forms import TarjetaForm
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

def form_tarjeta(request):
    datos={
        'form' : TarjetaForm()
    }
    if request.method == 'POST':
        
        formulario = TarjetaForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            datos ["mensaje"] = "GUARDADO EXITOSAMENTE"

    return render(request, 'core/form_tarjeta.html', datos)


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
