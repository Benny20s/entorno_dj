from django.urls import path
from .views import inicio, Poleras

urlpatterns = [
    path('',inicio, name="inicio" ),
    path('poleras', Poleras, name="poleras")
]

