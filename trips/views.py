from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic

from trips.models import Trip, TripDeparture
from trips.forms import TripForm, TripDepartureForm


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


class TripCreateView(generic.edit.CreateView):
    form_class = TripForm
    model = Trip


class TripUpdateView(generic.edit.UpdateView):
    model = Trip


class TripDeleteView(generic.edit.DeleteView):
    model = Trip
    success_url = reverse_lazy('trips:index')


class DepartureCreateView(generic.edit.CreateView):
    form_class = TripDepartureForm
    model = TripDeparture

    def get_success_url(self):
        return reverse_lazy("trips:trip_detail", args=(self.object.trip.id,))


class DepartureDetailView(generic.DetailView):
    model = TripDeparture
    template_name = 'trips/departure_detail.html'


class DepartureDeleteView(generic.edit.DeleteView):
    model = TripDeparture
    success_url = reverse_lazy("trips:departures")


class DeparturesView(generic.ListView):
    template_name = 'trips/departures.html'
    context_object_name = 'departure_list'

    def get_queryset(self):
        """
        Return a paginated list of existing trips departures
        """
        return TripDeparture.objects.order_by('-start_date')[:5]
