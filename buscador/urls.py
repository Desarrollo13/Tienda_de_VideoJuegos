from django.urls import path
from . import views

app_name = 'buscador'

urlpatterns=[
    path('',views.buscar_juegos, name='buscar_juegos'),
   
]