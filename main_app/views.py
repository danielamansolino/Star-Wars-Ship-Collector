import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ship, Crew, Photo
from .forms import MaintenanceForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def ships_index(request):
    ships = Ship.objects.filter(user=request.user)
    return render(request, 'ships/index.html', {
        'ships': ships
    })

@login_required
def ships_detail(request, ship_id):
    ship = Ship.objects.get(id=ship_id)
    id_list = ship.crew.all().values_list('id')
    crew_ship_doesnt_have = Crew.objects.exclude(id__in=id_list)
    maintenance_form = MaintenanceForm()
    return render(request, 'ships/detail.html', {'ship': ship, 'maintenance_form': maintenance_form, 'crew': crew_ship_doesnt_have})

class ShipCreate(LoginRequiredMixin, CreateView):
    model = Ship
    fields = ['name', 'created_by', 'ship_class', 'maximum_speed']
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class ShipUpdate(LoginRequiredMixin, UpdateView):
    model = Ship
    fields = ['created_by', 'ship_class', 'maximum_speed']

class ShipDelete(LoginRequiredMixin, DeleteView):
    model = Ship
    success_url = '/ships'

@login_required
def add_task(request, ship_id ):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.ship_id = ship_id
        new_maintenance.save()
    return redirect('detail', ship_id=ship_id)

class CrewList(LoginRequiredMixin, ListView):
  model = Crew
  
class CrewDetail(LoginRequiredMixin, DetailView):
  model = Crew

class CrewCreate(LoginRequiredMixin, CreateView):
  model = Crew
  fields = '__all__'

class CrewUpdate(LoginRequiredMixin, UpdateView):
  model = Crew
  fields = ['name', 'rank', 'color']

class CrewDelete(LoginRequiredMixin, DeleteView):
  model = Crew
  success_url = '/crew'

@login_required
def assoc_crew(request, ship_id, crew_id):
   Ship.objects.get(id=ship_id).crew.add(crew_id)
   return redirect('detail', ship_id=ship_id)

@login_required
def unassoc_crew(request, ship_id, crew_id):
   Ship.objects.get(id=ship_id).crew.remove(crew_id)
   return redirect('detail', ship_id=ship_id)

@login_required
def add_photo(request, ship_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, ship_id=ship_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', ship_id=ship_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)