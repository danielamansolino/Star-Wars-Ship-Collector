from django.db import models
from django.urls import reverse

CHORES = (
    ('C', 'Cleaning'),
    ('H', 'Hypermatter Fuel Refill'),
    ('A', 'AMMO Recharge'),
    ('S', 'Shield Recharge')
)

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
