from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

CHORES = (
    ('C', 'Cleaning'),
    ('H', 'Hypermatter Fuel Refill'),
    ('A', 'AMMO Recharge'),
    ('S', 'Shield Recharge')
)

# Create your models here.

class Crew(models.Model):
    name = models.CharField(max_length=50)
    rank = models.CharField(max_length=30)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('crew_detail', kwargs={'pk': self.id})


class Ship(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    ship_class = models.TextField(max_length=250)
    maximum_speed = models.IntegerField()
    crew = models.ManyToManyField(Crew)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'ship_id': self.id})
    
    def task_for_today(self):
        return self.maintenance_set.filter(date=date.today()).count() >= len(CHORES)
    
class Maintenance(models.Model):
    date = models.DateField('Maintenance Date')
    chore = models.CharField(
        max_length=1,
        choices=CHORES,
        default=CHORES[1][0]
    )
    ship = models.ForeignKey(
        Ship,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_chore_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for ship_id: {self.ship_id} @{self.url}"
