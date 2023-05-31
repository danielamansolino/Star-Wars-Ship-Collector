from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ship

# ships = [
#   {'name': 'Millennium Falcon', 'created_by': 'Corellian Engineering Corporation', 'class': 'Light freighter', 'maximum_speed': 1200},
#   {'name': 'X Wing', 'created_by': 'Incom Corporation', 'class': 'Starfighter', 'maximum_speed': 1050},
#   {'name': 'Imperial Star Destroyer', 'created_by': 'Kuat Drive Yards', 'class': 'Star Destroyer', 'maximum_speed':975},
  
# ]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def ships_index(request):
    ships = Ship.objects.all()
    return render(request, 'ships/index.html', {
        'ships': ships
    })

def ships_detail(request, ship_id):
    ship = Ship.objects.get(id=ship_id)
    return render(request, 'ships/detail.html', {'ship': ship})

class ShipCreate(CreateView):
    model = Ship
    fields = '__all__'

class ShipUpdate(UpdateView):
  model = Ship
  fields = ['created_by', 'ship_class', 'maximum_speed']

class ShipDelete(DeleteView):
  model = Ship
  success_url = '/ships'
