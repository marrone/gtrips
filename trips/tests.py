from django.test import TestCase
from django.core.urlresolvers import reverse

from trips.models import Trip


def create_trip(name):
    """
    Create a trip with the given name
    """
    return Trip.objects.create(name=name)


class TripIndexViewTests(TestCase):
    def test_index_view_with_no_trips(self):
        """
        If no trips exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('trips:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No trips exist.")
        self.assertQuerysetEqual(response.context['trip_list'], [])

    def test_index_view_with_a_single_trip(self):
        """
        Any existing trips should display on the index page
        """
        create_trip(name="First Trip.")
        response = self.client.get(reverse('trips:index'))
        self.assertQuerysetEqual(
            response.context['trip_list'],
            ['<Trip: First Trip.>']
        )

    def test_index_view_with_multiple_trips(self):
        """
        Multiple trips display on the index page
        """
        create_trip(name="First Trip.")
        create_trip(name="Second Trip.")
        create_trip(name="Third Trip.")
        response = self.client.get(reverse('trips:index'))
        self.assertQuerysetEqual(
            response.context['trip_list'],
            ['<Trip: First Trip.>', '<Trip: Second Trip.>', '<Trip: Third Trip.>']
        )

    def test_index_view_is_paginated(self):
        """
        Index should display pages of 10 trips
        """
        trips = [create_trip(name="Trip {0}".format(i)) for i in range(35)]
        trips = map(repr, sorted(trips, key=lambda t: t.name))
        response = self.client.get(reverse("trips:index"))
        self.assertQuerysetEqual(response.context["trip_list"], trips[:10])
        self.assertContains(response, "Page")
        self.assertContains(response, "of 4")

    def test_index_view_filters_by_search_term(self):
        """
        Index trips can be filterd by search term
        """
        create_trip(name="Foo")
        create_trip(name="Bar")
        create_trip(name="Baz")
        response = self.client.get(reverse("trips:index_search", args=["Ba"]))
        self.assertQuerysetEqual(response.context["trip_list"], ["<Trip: Bar>", "<Trip: Baz>"])
        self.assertContains(response, "like \"Ba\"")
