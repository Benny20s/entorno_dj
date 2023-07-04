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
    
    contexto = {
        'p':producto
    }
    if request.method == 'POST':
        producto.delete()
        return redirect('ListarProducto')
    
    return render(request, 'aplicacion/crud_producto/eliminar.html', contexto)

def ModificarProducto(request, id):
    producto = Producto.objects.get(id=id)
    tipo_producto = Producto.TIPO
    
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        tipo = request.POST['tipo']
        desc = request.POST['desc']
        color = request.POST['color']
        img = request.POST['img']
        
        producto.nombre = nombre
        producto.precio=precio
        producto.tipo_producto = tipo
        producto.descripcion=desc
        producto.color=color
        producto.imagen=img
        producto.save()
        return redirect('ListarProducto')

    contexto = {
        'p': producto,
        'tipo': tipo_producto
    }
    return render(request, 'aplicacion/crud_producto/modificar.html', contexto)

def ListarProducto(request):
    productos = Producto.objects.all()
    
    contexto = {
        'producto': productos,
    }
    
    return render(request, 'aplicacion/crud_producto/listar.html', contexto)

def AgregarProducto(request):
    tipo_producto = Producto.TIPO
    contexto = {
        'msg': '',
        'tipo': tipo_producto
    }
    
    if request.method == 'POST':
        nombre = request.POST['nombre']
        tipo = request.POST['tipo']
        precio = request.POST['precio']
        desc = request.POST['desc']
        color = request.POST['color']
        img = request.POST['img']
        
        product = Producto()
        product.nombre = nombre
        product.tipo_producto = tipo
        product.precio = precio
        product.descripcion = desc
        product.color = color
        product.imagen = img
        product.save()
        
        contexto['msg'] = 'Plato guardado correctamente'
    
    return render(request, 'aplicacion/crud_producto/agregar.html', contexto)

def carrito(request):
    return render(request, 'aplicacion/carrito/carri.html')