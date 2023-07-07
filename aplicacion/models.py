from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Producto(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    precio=models.IntegerField(null=False, default=1)
    stock = models.BigIntegerField(null=False, default=1)
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    color=models.CharField(max_length=20)
    imagen=models.CharField(max_length=500, null=False, blank=False)
    
    TIPO = [
        ('FUNKO', 'FUNKO'),
        ('POLERON', 'POLERON'),
        ('POLERAS', 'POLERAS'),
        ('MAS', 'MAS')
    ]
    tipo_producto = models.CharField(null=False, blank=False, choices=TIPO, max_length=20)
    def __str__(self):
        return str(f'{self.nombre}')

class CarritoCompra(models.Model):
    id_carrito = models.UUIDField(primary_key=True, default=uuid.uuid4)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    productos = models.ManyToManyField(Producto, through='ElementoCarrito')
    total_venta = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    
    TIPO_ESTADO = [
        ('FINALIZADO', 'FINALIZADO'),
        ('PENDIENTE', 'PENDIENTE'),
    ]
    
    estado = models.CharField(max_length=15, choices=TIPO_ESTADO, default='PENDIENTE')
    
    def __str__(self):
        return str(f'Carrito de {self.cliente.username} - estado: {self.estado}')
    
    def cancular_totalV(self):
        self.total_venta = sum(elemento.sub_total for elemento in self.elementocarrito_set.all())


class ElementoCarrito(models.Model):
    carrito = models.ForeignKey(CarritoCompra, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.DecimalField(max_digits=3, decimal_places=0, default=1)
    sub_total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    
    def calcular_subT(self):
        self.sub_total = self.cantidad*self.producto.precio
    
    def __str__(self):
        return str(f'{self.producto.nombre} - carrito de: {self.carrito.cliente.username} - ({self.carrito.estado})')
    


