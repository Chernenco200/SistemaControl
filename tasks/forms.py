from django import forms

from django.forms import ModelForm
from .models import Task, Cliente, Producto, Empresa

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']



class ClienteForm(forms.ModelForm):
    class Meta:
        imagen = forms.ImageField()
        model = Cliente
        fields = ('codigo','nombre', 'telefono','imagen')
        labels = {
            'codigo': 'Código: ',
            'telefono': 'Telefono: ',
            'nombre': 'Descripcion: ',
            'imagen': 'Imagen: '
        }

class EditarClienteForm(forms.ModelForm):

    class Meta:
        #imagen = forms.ImageField()
        imagen = forms.ImageField()
        model = Cliente
        fields = ('codigo','nombre', 'telefono','imagen')
        labels = {
            'codigo': 'Código: ',
            'telefono': 'Telefono: ',
            'nombre': 'Descripcion: ',
            'imagen': 'Imagen: '

        }

        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
        }





class InventarioForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('cantidad',)
        labels = {
            'cantidad': 'Cantidad real: '
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        imagen = forms.ImageField()
        model = Producto
        fields = ('codigo','descripcion', 'imagen', 'costo','iva', 'precio', 'cantidad',  'unidad', 'porcion', 'unidad_venta' ,'servicio', 'barcode')
        labels = {
            'codigo': 'Código interno:',
            'descripcion': 'Descripción: ',
            'imagen': 'Imagen: ',
            'costo': 'Costo: ',
            'iva': 'IVA %: ',
            'precio': 'Precio unit. : ',
            'cantidad': 'Cantidad: ',
            'barcode': 'Código de barras: ',
            'servicio': ' ¿Es servicio?: ', 
            'porcion': 'Relación unidad venta por unidad de compra: (Ejemp. 24 x 1, 1 x 1) ',
            'unidad_venta': 'Unidad venta: '
        }
    
class EditarProductoForm(forms.ModelForm):

    class Meta:
        imagen = forms.ImageField()
        model = Producto
        fields = ('codigo', 'descripcion', 'imagen','costo','iva', 'unidad', 'precio', 'porcion', 'unidad_venta' ,'servicio','barcode')
        labels = {
            'codigo': 'Código:',
            'descripcion': 'Descripción: ',
            'imagen': 'Imagen: ',
            'costo': 'Costo: ',
            'iva': 'IVA %: ',
            'precio': 'Precio unit. : ',
            'barcode': 'Código de barras: ',
            'servicio': ' ¿Es servicio?: ', 
            'porcion': 'Relación unidad venta por unidad de compra: (Ejemp. 24 x 1, 1 x 1) ',
            'unidad_venta': 'Unidad venta: '
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'id': 'codigo_editar'}),
            'descripcion': forms.TextInput(attrs={'id': 'descripcion_editar'}),
            'costo': forms.NumberInput(attrs={'id': 'costo_editar'}),
            'iva': forms.NumberInput(attrs={'id': 'iva_editar'}),
            'precio': forms.NumberInput(attrs={'id': 'precio_editar'}),
            'unidad': forms.Select(attrs={'id': 'unidad_editar'}),
            'porcion': forms.NumberInput(attrs={'id': 'porcion_editar'}),
            'barcode': forms.TextInput(attrs={'id': 'barcode_editar'}),
            'servicio': forms.CheckboxInput(attrs={'id': 'servicio_editar'}),
            'unidad_venta': forms.Select(attrs={'id': 'unidad_venta_editar'}),
        }

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nombre','domicilio', 'telefono', 'imagen', 'moneda')
        labels = {
            'nombre': 'Nombre:',
            'telefono': 'Contacto: ',
            'domicilio': 'Domicilio: ', 
            'imagen': 'Imagen: ',
            'moneda': 'Moneda: '
        }

class AddProductoForm(forms.ModelForm):
    class Meta:
        imagen = forms.ImageField()
        model = Producto
        fields = ('codigo','descripcion', 'imagen', 'costo','iva', 'precio', 'cantidad',  'unidad', 'porcion', 'unidad_venta' ,'servicio', 'barcode')
        labels = {
            'codigo': 'Código interno:',
            'descripcion': 'Descripción: ',
            'imagen': 'Imagen: ',
            'costo': 'Costo: ',
            'iva': 'IVA %: ',
            'precio': 'Precio unit. : ',
            'cantidad': 'Cantidad: ',
            'barcode': 'Código de barras: ',
            'servicio': ' ¿Es servicio?: ', 
            'porcion': 'Relación unidad venta por unidad de compra: (Ejemp. 24 x 1, 1 x 1) ',
            'unidad_venta': 'Unidad venta: '
        }