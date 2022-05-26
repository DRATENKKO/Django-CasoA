from django.db import models
# Create your models here.

#modelo SQLITO
class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True)
    nombreCategoria=models.CharField(max_length=50)
    def __str__(self):
        return self.nombreCategoria

class Vehiculo(models.Model):
    patente=models.CharField(max_length=50,primary_key=True)
    marca=models.CharField(max_length=20)
    modelo=models.CharField(max_length=20,null=True,blank=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.patente

class Tarjeta(models.Model):
    numeroTarjeta= models.CharField(max_length=20, primary_key=True)
    nombre= models.CharField(max_length=100)
    expiracion = models.DateField()
    cvv = models.IntegerField()
    def __str__(self):
        return self.nombre

