from django.test import TestCase
from django.test import Client
from airports.models import Airport, Runway
from flights.models import Flight
from datetime import datetime


class FlightTestCase(TestCase):
    client = None

    def setUp(self):
        a1 = Airport.objects.create(name="Myrtle Beach International Airport", airport_code="MYR",
                                    address="1100 Jet Port Road", city="Myrtle Beach",
                                    state="SC", zipcode="29577", is_open=True)
        a2 = Airport.objects.create(name="Hartsfield - Jackson International Airport", airport_code="ATL",
                                    address="1100 Jet Port Road", city="Myrtle Beach",
                                    state="SC", zipcode="29577", is_open=True)
        Flight.objects.create(origin=a1, destination=a2,
                              departure=datetime.now(), arrival=datetime.now(),
                              aircraft_type="CRJ9")
        Flight.objects.create(origin=a2, destination=a1,
                              departure=datetime.now(), arrival=datetime.now(),
                              aircraft_type="B747")
        Runway(runway_number=18, runway_designation="N", length=9503, width=150, airport=a1).save()
        Runway(runway_number=36, runway_designation="N", length=9503, width=150, airport=a1).save()
        self.client = Client()

    def test_index_path(self):
        response = self.client.get('/flights/')
        self.assertEqual(200, response.status_code)

    def test_search_path(self):
        response = self.client.get('/flights/search/MYR/MCO/')
        self.assertEqual(200, response.status_code)
