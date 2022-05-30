from django import forms
from django.forms import ModelForm
from .models import Tarjeta



#CLASE TARJETA
class TarjetaForm(ModelForm):



    class Meta:
        model = Tarjeta
        fields = '__all__'
        