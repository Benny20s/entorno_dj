from django.shortcuts import render
from .models import poleras, polerones, funko, mas

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
    return render(request, 'aplicacion/registration/cuenta.html')