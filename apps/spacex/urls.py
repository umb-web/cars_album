from django.urls import path
from . import views

urlpatterns = [
    path("", views.spacex, name="spacex"),
]
