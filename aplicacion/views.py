from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(request):
    return render(request, 'aplicacion/inicio.html')

def Poleras(request):
    Poleras= Producto.objects.filter(tipo_producto='PA')

    contexto={
        "polera": Poleras
    }
    return render(request, 'aplicacion/poleras.html', contexto)

def Polerones(request):
    Polerones=Producto.objects.filter(tipo_producto='PO')

    contexto={
        "polerones": Polerones
    }
    return render(request, 'aplicacion/polerones.html', contexto)

def Funko(request):
    Funko=Producto.objects.filter(tipo_producto='F')

    contexto={
        "funko": Funko
    }
    return render(request, 'aplicacion/funko.html', contexto)

def Mas(request):
    Mas=Producto.objects.filter(tipo_producto='M')

    contexto={
        "mas": Mas
    }
    return render(request, 'aplicacion/mas.html', contexto)

def Cuenta(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        usr = authenticate(username=username, password=password)
        
        if usr is not None:
            login(request, usr)
            return redirect('inicio')
    return render(request, 'aplicacion/registration/cuenta.html')


def CrearCuenta(request):
    contexto = {
        'msg': ''
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            contexto['msg'] = 'El usuario ingresado ya existe'
        else:
            usr = User()
            usr.username = username
            usr.set_password(password)
            
            usr.save()
            
            login(request, usr)
            return redirect('inicio')
        
    return render(request, 'aplicacion/registration/crearcuenta.html', contexto)

def EliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('inicio')
    
    return render(request, 'aplicacion/confirmacion.html')

def ModificarProducto(request, id):
    producto = Producto.objects.get(id=id)
    
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        desc = request.POST['descripcion']
        color = request.POST['color']
        img = request.POST['imagen']
        
        producto.nombre = nombre
        producto.precio=precio
        producto.descripcion=desc
        producto.color=color
        producto.imagen=img
        producto.save()
        return redirect('inicio')

    contexto = {
        'p': producto
    }
    return render(request, 'aplicacion/modificar_producto.html')