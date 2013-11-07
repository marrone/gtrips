from django.db import models

# Create your models here.

class Trip(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class TripDeparture(models.Model):
    trip = models.ForeignKey(Trip)
    start_date = models.DateTimeField()

    def __unicode__(self):
        return "{0} -> {1}".format(self.trip.name, self.start_date)
