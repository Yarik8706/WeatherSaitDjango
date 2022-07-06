from django.shortcuts import render
import requests
from .forms import CityForm
from weather.models import City


def index(request):
    appid = "1c4e2aad08b8be8cd1e07989f1c80d8f"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities_info = []
    cities = City.objects.all()

    for i in cities:
        res = requests.get(url.format(i.name)).json()
        cities_info.append({
            'city': i.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        })

    context = {
        'info': cities_info, 'form': form
    }

    return render(request, 'weather/index.html', context)
