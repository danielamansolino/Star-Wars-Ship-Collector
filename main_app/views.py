from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Ship, Crew
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
    id_list = ship.crew.all().values_list('id')
    crew_ship_doesnt_have = Crew.objects.exclude(id__in=id_list)
    maintenance_form = MaintenanceForm()
    return render(request, 'ships/detail.html', {'ship': ship, 'maintenance_form': maintenance_form, 'crew': crew_ship_doesnt_have})

class ShipCreate(CreateView):
    model = Ship
    fields = ['name', 'created_by', 'ship_class', 'maximum_speed']

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

class CrewList(ListView):
  model = Crew
  
class CrewDetail(DetailView):
  model = Crew

class CrewCreate(CreateView):
  model = Crew
  fields = '__all__'

class CrewUpdate(UpdateView):
  model = Crew
  fields = ['name', 'rank', 'color']

class CrewDelete(DeleteView):
  model = Crew
  success_url = '/crew'

def assoc_crew(request, ship_id, crew_id):
   Ship.objects.get(id=ship_id).crew.add(crew_id)
   return redirect('detail', ship_id=ship_id)

def unassoc_crew(request, ship_id, crew_id):
   Ship.objects.get(id=ship_id).crew.remove(crew_id)
   return redirect('detail', ship_id=ship_id)
   
    