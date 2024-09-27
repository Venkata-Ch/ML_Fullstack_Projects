from django.test import TestCase
from .models import Plane
import logging
log = logging.getLogger()
class PlaneTestcase(TestCase):
    def setUp(self):
        pass
    def test_data(self):
        try:
            travel_info = Plane.objects.get(airline="Vistara")

            if travel_info:
                print(travel_info)
            flights_stops = Plane.objects.filter(stops=2)
            if flights_stops:
                print(flights_stops)

            log.info("Data Uploaded successfully")

            # recommendation_test =

        except Exception as error:
            return str(error)
