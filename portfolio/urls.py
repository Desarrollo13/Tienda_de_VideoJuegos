from django.urls import path
from . import views
from .views import api_demo

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path("api-demo/", api_demo, name="api_demo"),
]
