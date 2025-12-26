from django.shortcuts import render

# Create your views here.
# vista de la pagina principal
def index(request):
    return render(request,"home/index.html")
def contacto(request):
    return render(request,"home/contacto.html")
