from django.shortcuts import render
import requests

URL = "https://api.spacexdata.com/v3/launches"


def spacex(request):
    response = requests.get(URL)
    data = response.json()
    return render(request, "pages/spacex.html", {"launches": data})


def launch_info(request, pk):
    LAUNCH_URL = f"https://api.spacexdata.com/v3/launches/{pk}/"
    response = requests.get(LAUNCH_URL)
    data = response.json()
    return render(request, "pages/launch.html", {"launch": data})


# Create your views here.
