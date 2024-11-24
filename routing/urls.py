from django.urls import path
from . import views

urlpatterns = [
    path('route/', views.ambulance_route, name='ambulance_route'),
]
