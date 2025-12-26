from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from catalogo.models import Juego

# Create your views here.
def lista_juegos(request):
    juegos=Juego.objects.all().order_by('id')#mantenemos un orden consistente
    paginator= Paginator(juegos,6)
    # obtemos el numero de pagina desde la url(pagina=2)
    page_number=request.GET.get('page')
    # obtenemos los objetos de esa pagina
    page_obj= paginator.get_page(page_number)
    
    # pasamos la plantilla como lista_juegos
    contexto_catalogo_juegos={'lista_juegos':page_obj}
    return render(request,'catalogo/lista_juegos.html',contexto_catalogo_juegos)

def detalle_juego(request,pk):
    # obtenemos el juego en concreto o mostramos un error 404 si no existe
    juego= get_object_or_404(Juego,pk=pk)
    # creamos el contexto que oasaremos a la plantilla
    contexto={'juego':juego}
    # renderizamos la plantilla detalle
    return render(request,'catalogo/detalle_juego.html',contexto)