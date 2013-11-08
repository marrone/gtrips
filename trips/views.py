import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic

from trips.models import Trip, TripDeparture
from trips.forms import TripForm, TripDepartureForm



class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    source: https://docs.djangoproject.com/en/1.5/topics/class-based-views/generic-editing/
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {'pk': self.object.pk, }
            return self.render_to_json_response(data)
        else:
            return response


class IndexView(generic.ListView):
    template_name = 'trips/index.html'
    context_object_name = 'trip_list'
    paginate_by = 10

    def get_queryset(self):
        """
        Return a paginated list of existing trips
        """
        return Trip.objects.order_by('name')[:10]


class TripDetailView(generic.DetailView):
    model = Trip
    template_name = 'trips/trip_detail.html'


class TripCreateView(generic.edit.CreateView):
    form_class = TripForm
    model = Trip


class TripUpdateView(generic.edit.UpdateView):
    form_class = TripForm
    model = Trip

    def get_success_url(self):
        return reverse_lazy("trips:trip_detail", args=(self.object.id,))


class TripDeleteView(generic.edit.DeleteView):
    model = Trip
    success_url = reverse_lazy('trips:index')


class DepartureCreateView(generic.edit.CreateView):
    form_class = TripDepartureForm
    model = TripDeparture

    def get_success_url(self):
        return reverse_lazy("trips:trip_detail", args=(self.object.trip_id,))


class DepartureUpdateView(generic.edit.UpdateView):
    form_class = TripDepartureForm
    model = TripDeparture

    def get_success_url(self):
        return reverse_lazy("trips:trip_detail", args=(self.object.trip_id,))


class DepartureDetailView(generic.DetailView):
    model = TripDeparture
    template_name = 'trips/departure_detail.html'


class DepartureDeleteView(AjaxableResponseMixin, generic.edit.DeleteView):
    model = TripDeparture

    def get_success_url(self):
        return reverse_lazy("trips:trip_detail", args=(self.object.trip_id,))


class DeparturesView(generic.ListView):
    template_name = 'trips/departures.html'
    context_object_name = 'departure_list'
    paginate_by = 10

    def get_queryset(self):
        """
        Return a paginated list of existing trips departures
        """
        return TripDeparture.objects.order_by('-start_date')
