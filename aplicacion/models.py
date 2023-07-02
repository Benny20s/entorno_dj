from django.db import models
import uuid

# Create your models here.

class Producto(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    precio=models.IntegerField()
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




