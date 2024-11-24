from django.shortcuts import render
from .utils import get_optimized_route, get_nearby_hospitals
import googlemaps
from django.conf import settings
def ambulance_route(request):
    if request.method == 'POST':
        start_location = request.POST.get('start_location')
        end_location = request.POST.get('end_location')
        mode = request.POST.get('mode')  # Get the selected mode from the form

        # Initialize Google Maps Client
        gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

        # Geocode the start and end locations
        start_geocode = gmaps.geocode(start_location)
        end_geocode = gmaps.geocode(end_location)

        # Extract lat/lng
        start_lat_lng = start_geocode[0]['geometry']['location']
        end_lat_lng = end_geocode[0]['geometry']['location']

        # Get optimized route
        route_data, distance, duration = get_optimized_route(start_lat_lng, end_lat_lng)

        # Get nearby hospitals based on the end location
        nearby_hospitals = get_nearby_hospitals(end_lat_lng)

        # Decide which template to render based on the mode
        if mode == 'normal':
            return render(request, 'routing/standard_mode.html', {
                'route_data': route_data,
                'distance': distance,
                'duration': duration,
                'hospitals': nearby_hospitals  # Pass sorted hospitals to the template
            })
        elif mode == 'emergency':
            return render(request, 'routing/emergency_mode.html', {
                'route_data': route_data,
                'distance': distance,
                'duration': duration,
                'hospitals': nearby_hospitals  # Pass sorted hospitals to the template
            })

    return render(request, 'routing/route_form.html')
