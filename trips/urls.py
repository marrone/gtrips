from django.conf.urls import patterns, url

from trips import views

urlpatterns = patterns("",
    # /trips/ list, optionally paged
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^page/(?P<page>\d+)/$', views.IndexView.as_view(), name='index'),
    # /trips crud
    url(r'^(?P<pk>\d+)/$', views.TripDetailView.as_view(), name='trip_detail'),
    url(r'^create/$', views.TripCreateView.as_view(), name='trip_create'),
    url(r'^(?P<pk>\d+)/edit/$', views.TripUpdateView.as_view(), name='trip_update'),
    url(r'^(?P<pk>\d+)/delete/$', views.TripDeleteView.as_view(), name='trip_delete'),
    # /departures/ list, optionally paged
    url(r'^departures/$', views.DeparturesView.as_view(), name='departures'),
    url(r'^departures/page/(?P<page>\d+)/$', views.DeparturesView.as_view(), name='departures'),
    # departures crud
    url(r'^departures/(?P<pk>\d+)/$', views.DepartureDetailView.as_view(), name='departure_detail'),
    url(r'^departures/create/$', views.DepartureCreateView.as_view(), name='departure_create'),
    url(r'^(?P<trip>\d+)/departures/create/$', views.DepartureCreateView.as_view(), name='departure_create'),
    url(r'^/departures/(?P<pk>\d+)/edit/$', views.DepartureUpdateView.as_view(), name='departure_update'),
    url(r'^departures/(?P<pk>\d+)/delete$', views.DepartureDeleteView.as_view(), name='departure_delete'),
)
