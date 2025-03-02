from django.shortcuts import render
import requests

URL = "https://api.spacexdata.com/v3/launches"


def spacex(request):
    response = requests.get(URL)
    data = response.json()
    return render(request, "pages/spacex.html", {"launches": data})


# Create your views here.
