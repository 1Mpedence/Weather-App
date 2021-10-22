from django.shortcuts import redirect, render
from .forms import CityForm
from .models import City
from datetime import datetime
import requests

# Create your views here.
def index(request):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c032106651b4a0d532b3c94e5581019d"    

    form = CityForm()
    
    if request.method == "POST":
        form = CityForm(request.POST)

        if form.is_valid():
            name = request.POST.get("name").capitalize()
            r = requests.get(api_url.format(name)).json()   
            City.objects.update_or_create(name=name, 
                                          defaults={'name': name, 
                                                    'icon_id': r['weather'][0]['icon'], 
                                                    'temperature': r["main"]["temp"], 
                                                    'description': r['weather'][0]['description'].capitalize()
                                                    }
                                         )
            return redirect("index")

    cities = City.objects.all().order_by("-created")
    context = {"cities": cities, "form": form}
    return render(request, "weather_app/index.html", context)

def delete(request, pk):
    city = City.objects.get(id=pk)
    city.delete()
    return redirect("index")

def delete_all(request):
    cities = City.objects.all()
    cities.delete()
    return redirect("index")