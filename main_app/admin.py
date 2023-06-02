from django.contrib import admin
from . models import Ship, Maintenance, Crew, Photo

# Register your models here.
admin.site.register(Ship)
admin.site.register(Maintenance)
admin.site.register(Crew)
admin.site.register(Photo)

