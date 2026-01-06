from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'portfolio/home.html')


# renderizado para la api

def api_demo(request):
    return render(request, "portfolio/api_demo.html")
