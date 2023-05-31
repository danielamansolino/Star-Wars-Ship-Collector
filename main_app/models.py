from django.db import models
from django.urls import reverse

# Create your models here.
class Ship(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    ship_class = models.TextField(max_length=250)
    maximum_speed = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'ship_id': self.id})