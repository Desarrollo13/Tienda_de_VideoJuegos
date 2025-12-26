from django.shortcuts import render, get_object_or_404
from .models import Noticia

def lista_noticias(request):
    noticias = Noticia.objects.filter(publicada=True).order_by('-creada')
    return render(request, 'noticias/lista.html', {'noticias': noticias})


def detalle_noticia(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug, publicada=True)
    return render(request, 'noticias/detalle_lista.html', {'noticia': noticia})
