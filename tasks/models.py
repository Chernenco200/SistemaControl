from django.db import models
from django.contrib.auth.models import User

from django.forms import model_to_dict
from django_resized import ResizedImageField
from datetime import date
from django.core.exceptions import ValidationError

# Create your models here.
TODAY = date.today()
# Create your models here.

ESTADOS = ( 
    ("Programado", "Programado"), 
    ("En espera", "En espera"), 
    ("En proceso", "En proceso"), 
    ("Atrasado", "Atrasado"),  
    ("Realizado", "Realizado")
    )

UNIDAD_COMPRA = ( 
    ("Pieza", "Pieza"),  
    ("Kg", "Kg"), 
    ("gramos", "gramos"),
    ("Lt", "Lt"), 
    ("Metro", "Metro"),  
    ("Caja", "Caja"), 
    ("Onza", "Onza"),
    ("Charola", "Charola"),
    ("Otro", "Otro")
    )

def validate_image(imagen):
    max_height = 100
    max_width = 100
    height = imagen.height 
    width = imagen.width
    if width > max_width or height > max_height:
        raise ValidationError("El largo de la imagen no debe superar los {} px y ancho de la imagen no deben superar los {} px".format(max_height, max_width))


def validate_image_equipo(imagen):
    max_height = 300
    max_width = 400
    height = imagen.height 
    width = imagen.width
    if width > max_width or height > max_height:
        raise ValidationError("El largo de la imagen no debe superar los {} px y ancho de la imagen no deben superar los {} px".format(max_height, max_width))


class Iva (models.Model):
    monto = models.DecimalField(max_digits=15, decimal_places=2, null=False)

    class Meta:
        verbose_name='iva'
        verbose_name_plural = 'iva'
    
    def __str__(self):
        return str(self.monto)

class Almacen (models.Model):
    codigo = models.CharField(max_length=255, unique=True, null=True, blank = True)
    nombre = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='almacen', null=True, blank=True)

    class Meta:
        verbose_name='almacen'
        verbose_name_plural = 'almacenes'
    
    def __str__(self):
        return self.nombre





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
  imagen = models.ImageField(upload_to='cliente', null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = 'clientes'
    verbose_name_plural = 'clientes'

  def __str__(self):
    return self.nombre


class Producto (models.Model):
    codigo = models.CharField(max_length=255, null=True, blank = True)
    descripcion =  models.CharField(max_length=255, unique=True, null=False)
    imagen = ResizedImageField(size=[100, 100], upload_to='productos', blank=True, null=True)
    costo = models.DecimalField(max_digits=20, decimal_places=2, null=False, default = 0)
    precio = models.DecimalField(max_digits=20, decimal_places=2, null=False, default =0)
    iva = models.DecimalField(max_digits=20, decimal_places=2, null=False, default =0)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2 , null=False,default=0)
    porcion = models.DecimalField(max_digits=20, decimal_places=2 , null=False,default=1)
    unidad = models.CharField(max_length=255, choices = UNIDAD_COMPRA, default='Pieza', null=False)
    unidad_venta = models.CharField(max_length=255, choices = UNIDAD_COMPRA, default='Pieza', null=False)
    servicio = models.BooleanField(default=False)
    barcode = models.CharField(max_length=255, unique=False, null=True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural = 'productos'
        order_with_respect_to = 'descripcion'
    
    def __str__(self):
        return self.descripcion

    def toJSON(self):
        item = model_to_dict(self, exclude=['imagen', 'created', 'updated'])
        return item

class Empresa (models.Model):
    nombre = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255, null=True)
    telefono = models.CharField(max_length=255, null=True)
    imagen = ResizedImageField(size=[100, 100], upload_to='empresa', blank=True, null=True)
    moneda = models.CharField(max_length=255, null=False, blank=False, default="$" )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='empresa'
        verbose_name_plural = 'empresa'
    
    def __str__(self):
        return self.nombre


class Egreso(models.Model):
    fecha_pedido = models.DateField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL , null=True , related_name='clientee')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    pagado = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    comentarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.BooleanField(default=True)
    desglosar = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True , null=True)

    class Meta:
        verbose_name='egreso'
        verbose_name_plural = 'egresos'
        order_with_respect_to = 'fecha_pedido'
    
    def __str__(self):
        return str(self.id)
   

class ProductosEgreso(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2 , null=False)
    precio = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)

    class Meta:
        verbose_name='producto egreso'
        verbose_name_plural = 'productos egreso'
        order_with_respect_to = 'created'
    
    def __str__(self):
        return self.producto
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item





class Venta(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    # Otros campos necesarios para la venta

    def __str__(self):
        return f"Venta de {self.nombre_cliente} - {self.fecha_venta}"
