from django.db import models

# Create your models here.

class poleras(models.Model):
    id=models.IntegerField(primary_key=True)
    precio=models.IntegerField()
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    color=models.CharField(max_length=20)
    imagen=models.CharField(max_length=500, null=False, blank=False)
    
    def __str__(self):
        return str(f'{self.nombre}')


class polerones(models.Model):
    id=models.IntegerField(primary_key=True)
    precio=models.IntegerField()
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    color=models.CharField(max_length=20)
    imagen=models.CharField(max_length=500, null=False, blank=False)
    
    def __str__(self):
        return str(f'{self.nombre}')

class funko(models.Model):
    id=models.IntegerField(primary_key=True)
    precio=models.IntegerField()
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    imagen=models.CharField(max_length=500, null=False, blank=False)
    
    def __str__(self):
        return str(f'{self.nombre}')

class mas(models.Model):
    id=models.IntegerField(primary_key=True)
    precio=models.IntegerField()
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    imagen=models.CharField(max_length=500, null=False, blank=False)

