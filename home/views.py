from django.shortcuts import render


# vista de la pagina principal
def index(request):
    return render(request,"home/index.html")
def contacto(request):
    return render(request,"home/contacto.html")
