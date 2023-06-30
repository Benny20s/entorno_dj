from django.shortcuts import render, redirect
from .models import poleras, polerones, funko, mas
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(request):
    return render(request, 'aplicacion/inicio.html')

def Poleras(request):
    Poleras=poleras.objects.all()

    contexto={
        "polera": Poleras
    }
    return render(request, 'aplicacion/poleras.html', contexto)

def Polerones(request):
    Polerones=polerones.objects.all()

    contexto={
        "polerones": Polerones
    }
    return render(request, 'aplicacion/polerones.html', contexto)

def Funko(request):
    Funko=funko.objects.all()

    contexto={
        "funko": Funko
    }
    return render(request, 'aplicacion/funko.html', contexto)

def Mas(request):
    Mas=mas.objects.all()

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