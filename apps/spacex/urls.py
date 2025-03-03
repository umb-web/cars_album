from django.urls import path
from . import views

urlpatterns = [
    path("", views.spacex, name="spacex"),
    path("<int:pk>/", views.launch_info, name="launch_info"),
]
