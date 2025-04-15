from django.contrib import admin
from .models import CarMake, CarModel

# Basic registration
admin.site.register(CarMake)
admin.site.register(CarModel)
