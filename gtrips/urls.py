from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gtrips.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^trips/', include('trips.urls', namespace="trips")),
    url(r'^admin/', include(admin.site.urls)),
)
