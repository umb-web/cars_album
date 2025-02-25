"""
URL configuration for album project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
Flujo

1. crear app
2. agregar la app al settings.py
3. en el urls.py del proyecto crear el path con el include
4. dentro de la app crear el urls.py
5. dentro de la app en el views.py crear las funciones para renderizar 
las paginas que estan dentro del urls.py
6. revisar si esta creada la carpeta pages, y dentro los archivos que queremos renderizar
7. mirar si queremos enviar algo a la pagina creada dentro de pages

"""
from django.contrib import admin
from django.urls import path, include
from .views import inicio

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio, name="inicio"),
    path("fotos/", include("apps.fotos.urls")),
    path("noticias/", include("apps.articulos.urls")),
]
