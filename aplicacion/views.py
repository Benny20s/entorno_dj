from django.shortcuts import render
from .models import poleras

# Create your views here.

def inicio(request):
    return render(request, 'aplicacion/inicio.html')

def Poleras(request):
    Poleras=poleras.objects.all()

    contexto={
        "polera": Poleras
    }
    return render(request, 'aplicacion/poleras.html', contexto)
