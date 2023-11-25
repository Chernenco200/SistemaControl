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
  create = models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = 'cliente'
    verbose_name_plural = 'clientes'

  def __str__(self):
    return self.nombre


class Produco(models.Model):    
  codigo = models.CharField(max_length=200)
  descripcion = models.CharField(max_length=200)
  costo = models.DecimalField(max_digits=15, decimal_places=2)
  cantidad = models.DecimalField(max_digits=15, decimal_places=2)
  create = models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = 'cliente'
    verbose_name_plural = 'clientes'

  def __str__(self):
    return self.nombre
