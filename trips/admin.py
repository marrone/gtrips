from django.contrib import admin

# Register your models here.
from trips.models import Trip, TripDeparture

admin.site.register(Trip)
admin.site.register(TripDeparture)
