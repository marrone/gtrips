from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views import generic
from trips.models import Trip, TripDeparture


class IndexView(generic.ListView):
    template_name = 'trips/index.html'
    context_object_name = 'trip_list'

    def get_queryset(self):
        """
        Return a paginated list of existing trips
        """
        return Trip.objects.order_by('name')[:5]


class TripDetailView(generic.DetailView):
    model = Trip
    template_name = 'trips/trip_detail.html'


class DeparturesView(generic.ListView):
    template_name = 'trips/departures.html'
    context_object_name = 'departure_list'

    def get_queryset(self):
        """
        Return a paginated list of existing trips departures
        """
        return TripDeparture.objects.order_by('-start_date')[:5]
