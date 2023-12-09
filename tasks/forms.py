from django import forms

from django.forms import ModelForm
from .models import Task, Cliente

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