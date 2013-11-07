from django import forms
from trips.models import Trip, TripDeparture


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip

class TripDepartureForm(forms.ModelForm):
    class Meta:
        model = TripDeparture
