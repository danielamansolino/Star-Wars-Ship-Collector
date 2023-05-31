from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ship
from .forms import MaintenanceForm

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
    maintenance_form = MaintenanceForm()
    return render(request, 'ships/detail.html', {'ship': ship, 'maintenance_form': maintenance_form})

class ShipCreate(CreateView):
    model = Ship
    fields = '__all__'

class ShipUpdate(UpdateView):
    model = Ship
    fields = ['created_by', 'ship_class', 'maximum_speed']

class ShipDelete(DeleteView):
    model = Ship
    success_url = '/ships'

def add_task(request, ship_id ):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.ship_id = ship_id
        new_maintenance.save()
    return redirect('detail', ship_id=ship_id)
