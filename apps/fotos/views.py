from django.shortcuts import render
from .models import Mifoto


# Create your views here.
def fotos(request):
    mis_fotos = Mifoto.objects.all()
    return render(request, "pages/fotos.html", {"fotos": mis_fotos})


# Create your views here.
