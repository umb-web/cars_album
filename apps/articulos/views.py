from django.shortcuts import render, get_object_or_404
from .models import Articulo


def noticias(request):
    noticias = Articulo.objects.all()
    return render(request, "pages/noticias.html", {"noticias": noticias})


def detalle_noticias(request, pk):
    noticia = get_object_or_404(Articulo, pk=pk)
    return render(request, "pages/noticia.html", {"noticia": noticia})
