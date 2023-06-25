from django.shortcuts import render
from .models import poleras, polerones, funko

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