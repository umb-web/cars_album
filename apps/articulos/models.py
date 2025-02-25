from django.db import models
from django.db import models


class Articulo(models.Model):
    titulo = models.CharField(max_length=90)
    resumen = models.CharField(max_length=2000)
    foto = models.ImageField(upload_to="noticias/")
    detalle = models.CharField(max_length=2000)
    publicada = models.BooleanField(default=True)
    fecha = models.DateTimeField(auto_now=True)
