from django.http import HttpResponse
from .models import Flight
from airports.models import Airport

def index(request):
    flights = Flight.objects.all()
    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code for f in flights])
    return HttpResponse('Listing all flights: ' + flight_list)

def flight_search(request, origin, destination):
    origin = Airport.objects.get(airport_code=origin)
    destination = Airport.objects.get(airport_code=destination)
    flights = Flight.objects.filter(origin=origin.id, destination=destination.id)
    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " + f.airline.airline_code for f in flights])
    return HttpResponse('Showing flights: ' + flight_list)