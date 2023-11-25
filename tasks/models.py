from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title + ' - ' + self.user.username


class Cliente(models.Model):    
  codigo = models.CharField(max_length=200)
  nombre = models.CharField(max_length=200)
  telefono = models.CharField(max_length=200)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = 'clientes'
    verbose_name_plural = 'clientes'

  def __str__(self):
    return self.nombre


class Producto(models.Model):    
  codigo = models.CharField(max_length=200)
  descripcion = models.CharField(max_length=200)
  imagen = models.ImageField(upload_to='productos',null=True,blank=True)
  costo = models.DecimalField(max_digits=15, decimal_places=2)
  cantidad = models.DecimalField(max_digits=15, decimal_places=2)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = 'producto'
    verbose_name_plural = 'productos'
    order_with_respect_to = 'descripcion'

  def __str__(self):
    return self.descripcion
