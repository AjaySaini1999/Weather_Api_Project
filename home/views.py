from signal import SIG_DFL
from django.shortcuts import render, HttpResponse

# Create your views here.
import requests


def index(request):
    city = request.GET.get('city', 'Delhi')

    data = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=2cd473cb17321b0c0bd791b210e5e5de')
    r = data.json()
    payload = {
        'city': r['name'],
        'weather': r['weather'][0]['main'],
        'icon': r['weather'][0]['icon'],
        'kelvin_temperature': int(r['main']['temp']),
        'celcius_temperature': int(r['main']['temp']-273),
        'pressure': r['main']['pressure'],
        'humidity': r['main']['humidity'],
        'description': r['weather'][0]['description'],
    }

    context = {'data': payload}
    return render(request, 'home.html', context)
