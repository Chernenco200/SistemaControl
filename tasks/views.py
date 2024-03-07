from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Task, Cliente, Producto, Empresa

from .forms import TaskForm, ClienteForm , EditarClienteForm, InventarioForm , ProductoForm, EditarProductoForm, EmpresaForm, AddProductoForm
from django.contrib import messages





# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})


@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {"tasks": tasks})

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {"tasks": tasks})


@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {"form": TaskForm, "error": "Error creating task."})


def home(request):
    return render(request, 'home.html')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tasks')

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task.'})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')





def ventas_view(request):
    return render(request, 'ventas.html')


def cliente_view(request):

    form_personal = ClienteForm()
    form_editar_personal = EditarClienteForm()
    personal = Cliente.objects.all()
    num_personal = len(personal)

    context = {
        'form_personal': form_personal,
        'form_editar_personal': form_editar_personal,
        'personal': personal,
        'num_personal': num_personal
    }
    return render(request, 'clientes.html', context)

def add_cliente_view(request):
    if request.POST:
        #print(request.POST)
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages.warning(request,"Cliente ya agregado o datos incorrectos")
                return redirect('Cliente')


    return redirect('Cliente')

def delete_cliente_view(request):
    if request.POST:
        if int(request.POST.get('id_personal_eliminar')) == 1:
            messages.warning(request, "No es posible eliminar este cliente")
            return redirect('Cliente')
        personal = Cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
        personal.delete()
        
    return redirect('Cliente')

def edit_cliente_view(request):
    if request.POST:
        producto = Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarClienteForm(
            request.POST, request.FILES, instance=producto)
        if form.is_valid:
            form.save()

    return redirect('Cliente')   




#@login_required(login_url='Login')
def inventario_view(request):
    
    form_producto = ProductoForm()
    form_editar_producto = EditarProductoForm()
    form_ajustar = InventarioForm()
    productos = Producto.objects.all()
    num_productos = len(productos)
    empresa = Empresa.objects.get(pk=1)
    moneda = empresa.moneda

    context = {
        'form_producto': form_producto,
        'form_editar_producto': form_editar_producto,
        'productos': productos,
        'num_productos': num_productos, 
        'form_ajustar_producto': form_ajustar,
        'moneda': moneda
    }
    return render(request, 'inventario.html', context)


#@login_required(login_url='Login')
def delete_producto_view(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get('id_producto_eliminar'))
        if producto.imagen:
            os.remove(producto.imagen.path)
        producto.delete()
        
    return redirect('Product')


#@login_required(login_url='Login')
def add_product_view(request):
    if request.POST:
        #print(request.POST)
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages.warning(request,"Producto ya agregado o datos incorrectos")
                return redirect('Product')


    return redirect('Product')


#@login_required(login_url='Login')
def edit_product_view(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get('id_producto_editar'))
        form = EditarProductoForm(
            request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()

    return redirect('Product')

#@login_required(login_url='Login')
def ajuste_product_view(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get('id_producto_ajustar'))
        form = InventarioForm(
            request.POST, request.FILES, instance=producto)
        if form.is_valid():
            ajuste = Ajuste(producto=producto, cantidad_registrada=float(request.POST["cantidadanterior"]),cantidad_real=float(request.POST["cantidad"]), fecha=HOY,responsable=request.user)
            form.save()
            ajuste.save()

    return redirect('Product')

def empresa_view(request):
    
    empresa = Empresa.objects.get(pk=1)
    form_empresa = EmpresaForm(instance=empresa)

    if request.POST:
        empresa = Empresa.objects.get(pk=1)
        form_empresa = EmpresaForm(
            request.POST, request.FILES, instance=empresa)
        if form_empresa.is_valid():
            form_empresa.save()
            form_empresa = EmpresaForm(instance=empresa)
            messages.info(request,"Cambios efectuados con éxito")
    context = {
        'form_empresa': form_empresa,
        'empresa': empresa
    }

    return render(request, 'empresa.html', context)




def producto_view(request):

    """form_personal = ClienteForm()
    form_editar_personal = EditarClienteForm()
    personal = Cliente.objects.all()
    num_personal = len(personal)"""

    productos = Producto.objects.all()
    form_add = AddProductoForm()
    context = {
        'productos':productos,
        'form_add' :form_add 

    }
    return render(request, 'productos.html', context)

def add_producto_view(request):
    if request.POST:
        #print(request.POST)
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages.warning(request,"Producto ya agregado o datos incorrectos")
                return redirect('Productos')


    return redirect('Productos')