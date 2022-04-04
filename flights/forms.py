from django import forms

class FlightForm(forms.Form):
    origin_airport = forms.CharField(label="Origin Airport", max_length=100)
    destination_airport = forms.CharField(label="Destination Airport", max_length=100)