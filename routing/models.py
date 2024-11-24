from django.db import models

class AmbulanceRequest(models.Model):
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ambulance Request from {self.start_location} to {self.end_location}"

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    total_ambulances = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Ambulance(models.Model):
    vehicle_number = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, related_name='ambulances')
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='ambulances')

    def __str__(self):
        return self.vehicle_number
