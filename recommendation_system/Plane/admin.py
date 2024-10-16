from django.contrib import admin
from .models import Plane


#Model registry
class PlaneAdministrator(admin.ModelAdmin):
    fields = ['airline','arrival_time','departure_time','passenger_class','duration']
    list_display = ['airline','passenger_class','stops','duration']
    search_fields = ['price','days_left']
admin.site.register(Plane,PlaneAdministrator)
