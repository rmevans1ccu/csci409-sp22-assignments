from django.test import TestCase
from django.test import Client
from airports.models import Airport, Runway
from flights.models import Flight, Airline
from datetime import datetime


class FlightTestCase(TestCase):
    client = None

    def setUp(self):
        airline = Airline.objects.create(airline_name="American Airlines", airline_code="AA")
        a1 = Airport.objects.create(name="Myrtle Beach International Airport", airport_code="MYR",
                                    address="1100 Jet Port Road", city="Myrtle Beach",
                                    state="SC", zipcode="29577", is_open=True)
        a2 = Airport.objects.create(name="Hartsfield - Jackson International Airport", airport_code="ATL",
                                    address="1100 Jet Port Road", city="Myrtle Beach",
                                    state="SC", zipcode="29577", is_open=True)
        Flight.objects.create(origin=a1, destination=a2,
                              airline=airline, flight_number=1309,
                              departure=datetime.now(), arrival=datetime.now(),
                              aircraft_type="CRJ9")
        self.client = Client()

    def test_index_path(self):
        response = self.client.get('/flights/')
        self.assertEqual(200, response.status_code)

    def test_search_path(self):
        response = self.client.get('/flights/search/MYR/MCO/')
        self.assertEqual(200, response.status_code)

    def test_origin_code(self):
        flight = Flight.objects.get(pk=1)
        self.assertEqual(flight.origin.airport_code, "MYR")

    def test_destination_code(self):
        flight = Flight.objects.get(pk=1)
        self.assertEqual(flight.destination.airport_code, "ATL")

    def test_flight_number(self):
        flight = Flight.objects.get(pk=1)
        self.assertEqual(flight.flight_number, 1309)
