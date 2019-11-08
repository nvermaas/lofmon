from django.contrib import admin
from .models import Station, Observation, StationObservation, Antenna, AntennaState, SensorData

# Register your models here.
admin.site.register(Station)
admin.site.register(Observation)
admin.site.register(StationObservation)
admin.site.register(Antenna)
admin.site.register(AntennaState)
admin.site.register(SensorData)