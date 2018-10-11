from django import forms
from .models import Flight



class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_no', 'depart_city', 'destination_city', 'date', 'date_time', 'status']