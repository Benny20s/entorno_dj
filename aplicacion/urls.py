from django.urls import path
from .views import inicio, Poleras, Polerones, Funko, Mas, Cuenta

urlpatterns = [
    path('',inicio, name="inicio" ),
    path('poleras', Poleras, name="poleras"), 
    path('polerones', Polerones, name="polerones"),
    path('funko', Funko, name="funko"),
    path('mas', Mas, name="mas"),
    path('cuenta',Cuenta, name="cuenta"),
]

