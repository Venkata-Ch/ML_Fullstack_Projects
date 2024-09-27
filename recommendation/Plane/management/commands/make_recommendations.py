from venv import logger

from django.core.management import BaseCommand
from ...models import Plane
import logging

log = logging.getLogger()


# To check if passenger_class are valid
def check_valid_airline(passenger_class: str) -> bool:
    if bool(passenger_class and not passenger_class.isspace()) and passenger_class != 'na':
        return True
    else:
        return False

#Content based filtering
def content_based_filtering(fl_list1: list, fl_list2: list):
    g1 = set(fl_list1)
    g2 = set(fl_list2)
    return float(len(g1.intersection(g2))/len(g1.union(g2)))

def content_similarity(fli_1: Plane,fli_2: Plane)-> float:
    if check_valid_airline(fli_1.passenger_class) and check_valid_airline(fli_2.passenger_class):
        fli1_ = fli_1.passenger_class.split()
        fli2_ = fli_2.passenger_class.split()
        return content_based_filtering(fli1_,fli2_)

    else:
        return 0

class Command(BaseCommand):
    help = 'Recommending Flights'

    def add_argument(self, parser):
        pass

    def handle(self, *args, **kwargs):
        try:
            FILTER_THRESHOLD = 0.8
            afternoon_flights = Plane.objects.filter(
                departure_time="Afternoon")
            mornings_flights = Plane.objects.filter(
                departure_time="Morning")
            # Start to generate recommendations in morning flights
            for morning_flight in mornings_flights:
                similarity_score = 0
                will_recommend = False
                for afternoon_flight in afternoon_flights:
                    # Similarity calculation between afternoon_flights and all morning flights
                    similarity = content_similarity(morning_flight, afternoon_flight)
                    if similarity >= similarity_score:
                        max_similarity = similarity
                    # early stop if the morning flights is similar enough
                    if max_similarity >= FILTER_THRESHOLD:
                        break
                # If morning_flight is similar enough to afternoon flights
                # Then recommend it
                if max_similarity > FILTER_THRESHOLD:
                    will_recommend = True
                    print(f"Recommended flight: {morning_flight.airline}")
                morning_flight.recommend = will_recommend
                morning_flight.save()

        except Exception as error:
            log.error(str(error))






