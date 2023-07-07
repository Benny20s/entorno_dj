from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio, name="inicio" ),
    path('poleras/', Poleras, name="poleras"), 
    path('polerones/', Polerones, name="polerones"),
    path('funko/', Funko, name="funko"),
    path('mas/', Mas, name="mas"),
    path('cuenta/',Cuenta, name="cuenta"),
    path('crearcuenta/', CrearCuenta, name="crearcuenta"),
    path('productos/', ListarProducto, name='ListarProducto'),
    path('AgregarProducto/', AgregarProducto, name='AgregarProducto'),
    path('ModificarProducto/<id>', ModificarProducto, name='ModificarProducto'),
    path('EliminarProducto/<id>', EliminarProducto, name='EliminarProducto'),
    path('carrito/',carrito, name="carrito"),
    path('agregar-carrito/<id>', agregar_carrito, name='agregar_carrito'),
    path('eliminar-carrito/<id>', eliminar_carrito, name='eliminar_carrito'),
]

