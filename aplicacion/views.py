from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(request):
    return render(request, 'aplicacion/inicio.html')

def Poleras(request):
    Poleras= Producto.objects.filter(tipo_producto='POLERAS')

    contexto={
        "polera": Poleras
    }
    return render(request, 'aplicacion/poleras.html', contexto)

def Polerones(request):
    Polerones=Producto.objects.filter(tipo_producto='POLERON')

    contexto={
        "polerones": Polerones
    }
    return render(request, 'aplicacion/polerones.html', contexto)

def Funko(request):
    Funko=Producto.objects.filter(tipo_producto='FUNKO')

    contexto={
        "funko": Funko
    }
    return render(request, 'aplicacion/funko.html', contexto)

def Mas(request):
    Mas=Producto.objects.filter(tipo_producto='MAS')

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
        
        contexto['msg'] = 'Producto guardado correctamente'
    
    return render(request, 'aplicacion/crud_producto/agregar.html', contexto)

def carrito(request):
    data = {
        'elemento_carrito': None,
        'rango_cantidad': None,
        'mensaje_error': ''
    }
    
    usuario = User.objects.get(username=request.user.username)
    carrito, created = CarritoCompra.objects.get_or_create(cliente=usuario, estado='PENDIENTE')
    
    elemento_carrito = ElementoCarrito.objects.filter(carrito=carrito)
    
    if elemento_carrito.exists():
        #Esto pasara si existen productos en el carrito
        data['elemento_carrito'] = elemento_carrito
        rango_cantidad = range(1, max(elemento.producto.stock for elemento in elemento_carrito) + 1)
        data['rango_cantidad'] = rango_cantidad
        
        #Esto pasara cuando presione el boton comprar 
        if request.method == 'POST':
            #AQUI SE AÑADE EL CODIGO DE COMPRAR
            for elemento in elemento_carrito:
                cantidad = request.POST.get('cantidad_{}'.format(elemento.producto.id))
                print(cantidad)
                elemento.cantidad = int(cantidad)
                elemento.calcular_subT()
                elemento.save()
                producto = Producto.objects.get(id=elemento.producto.id)
                cantidad_int = int(cantidad)
                producto.stock -= cantidad_int
                producto.save()

            carrito.estado = "FINALIZADO"
            carrito.cancular_totalV()
            carrito.save()

            return redirect(to="inicio")
    return render(request, 'aplicacion/carrito/carri.html', data)

def agregar_carrito(request, id):
    
    id = uuid.UUID(id)
    producto = Producto.objects.get(id=id)
    usuario = User.objects.get(username=request.user.username)
    
    carrito, created = CarritoCompra.objects.get_or_create(cliente=usuario, estado='PENDIENTE')
    print(carrito.id_carrito)
    elemento_carrito, created = ElementoCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not created:
        elemento_carrito.cantidad += 1
        elemento_carrito.calcular_subT()
    
    elemento_carrito.cantidad = 1
    #print(elemento_carrito.producto.precio + ' ' + elemento_carrito.cantidad)
    elemento_carrito.calcular_subT()
    elemento_carrito.save()
    
    return redirect(to='carrito')

def eliminar_carrito(request, id):
    producto = Producto.objects.get(id=id)
    usuario = User.objects.get(username=request.user.username)
    carrito = CarritoCompra.objects.get(cliente=usuario, estado='PENDIENTE')
    
    elemento_carrito = ElementoCarrito.objects.get(carrito=carrito, producto=producto)
    
    elemento_carrito.delete()
    return redirect(to='carrito')

def cerrar_sesion(request):
    logout(request)
    return redirect(to='inicio')