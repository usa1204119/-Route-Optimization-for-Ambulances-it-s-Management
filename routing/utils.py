import googlemaps
from django.conf import settings
from geopy.distance import geodesic

def get_optimized_route(start_lat_lng, end_lat_lng):
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

    # Request directions from Google Maps API with traffic data
    directions = gmaps.directions(
        origin=f"{start_lat_lng['lat']},{start_lat_lng['lng']}",
        destination=f"{end_lat_lng['lat']},{end_lat_lng['lng']}",
        mode="driving",
        departure_time="now",  # 'now' for real-time traffic data
        optimize_waypoints=True,
        alternatives=False
    )

    # Extract distance and duration with traffic
    leg = directions[0]['legs'][0]  # The first route
    distance = leg['distance']['text']  # e.g., "12.3 km"
    duration = leg['duration_in_traffic']['text']  # e.g., "20 mins"

    return directions, distance, duration

def get_nearby_hospitals(lat_lng, radius=5000):
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    
    # Search for hospitals within the radius
    places_result = gmaps.places_nearby(
        location=lat_lng,
        radius=radius,
        type='hospital'
    )
    
    # Extract relevant data
    hospitals = []
    for place in places_result['results']:
        # Calculate the distance from the destination to each hospital
        hospital_location = (place['geometry']['location']['lat'], place['geometry']['location']['lng'])
        destination_location = (lat_lng['lat'], lat_lng['lng'])
        distance = geodesic(destination_location, hospital_location).km
        
        hospitals.append({
            'name': place['name'],
            'lat': hospital_location[0],
            'lng': hospital_location[1],
            'address': place.get('vicinity', ''),
            'distance': round(distance, 2)  # Round the distance to 2 decimal places
        })

    # Sort hospitals by distance
    hospitals_sorted = sorted(hospitals, key=lambda x: x['distance'])
    
    return hospitals_sorted
