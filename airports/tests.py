from django.test import TestCase
from django.test import Client
from airports.models import Airport, Runway


class AirportTestCase(TestCase):
    client = None

    def setUp(self):
        a1 = Airport.objects.create(name="Myrtle Beach International Airport", airport_code="MYR",
                                    address="1100 Jet Port Road", city="Myrtle Beach",
                                    state="SC", zipcode="29577", is_open=True)
        Runway(runway_number=18, runway_designation="N", length=9503, width=150, airport=a1).save()
        Runway(runway_number=36, runway_designation="N", length=9503, width=150, airport=a1).save()
        self.client = Client()

    def test_index_path(self):
        response = self.client.get('/airports/')
        self.assertEqual(200, response.status_code)

    def test_search_path(self):
        response = self.client.get('/airports/MYR')
        self.assertEqual(200, response.status_code)

    def test_myr_airport_name(self):
        myr = Airport.objects.get(airport_code="MYR")
        self.assertEqual(myr.name, "Myrtle Beach International Airport")

    def test_myr_airport_address(self):
        myr = Airport.objects.get(airport_code="MYR")
        self.assertEqual(myr.address, "1100 Jet Port Road")

    def test_myr_airport_city(self):
        myr = Airport.objects.get(airport_code="MYR")
        self.assertEqual(myr.city, "Myrtle Beach")

    def test_myr_airport_state(self):
        myr = Airport.objects.get(airport_code="MYR")
        self.assertEqual(myr.state, "SC")

    def test_myr_airport_zipcode(self):
        myr = Airport.objects.get(airport_code="MYR")
        self.assertEqual(myr.zipcode, "29577")

    def test_myr_airport_is_open(self):
        myr = Airport.objects.get(airport_code="MYR")
        self.assertEqual(myr.is_open, True)

    def test_myr_runway_count(self):
        myr = Airport.objects.get(airport_code="MYR")
        self.assertEqual(myr.runway_set.count(), 2)
