from django.conf.urls import patterns, url

from trips import views

urlpatterns = patterns("",
    # /trips/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /trips/5/
    url(r'^(?P<pk>\d+)/$', views.TripDetailView.as_view(), name='trip_detail'),
    # /departures/
    url(r'^departures/$', views.DeparturesView.as_view(), name='departures'),
    # /trips/5/departures/
    #url(r'^(?P<pk>\d+)/departures/$', views.DeparturesView.as_view(), name='tripdepartures'),
    # /trips/create/
    #url(r'^create/$', views.create_trip, name='vote'),
)
