from django.contrib import admin
from .models import Hospital, Ambulance, Driver

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'total_ambulances')

@admin.register(Ambulance)
class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'vehicle_model', 'driver', 'hospital')

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'license_number', 'contact_number')
