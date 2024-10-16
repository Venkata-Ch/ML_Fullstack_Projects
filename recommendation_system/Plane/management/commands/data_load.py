import pandas as pd
from django.core.management import BaseCommand
from ...models import Plane
import logging

log = logging.getLogger()

class Command(BaseCommand):

    def add_argument(self, parser):
        parser.add_argument('--pythonpath',type=str,help="Load travel data")

    def handle(self, *args, **kwargs):
        try:
            log.info("Removing any previously loaded data")
            Plane.objects.all().delete()
            path = kwargs['pythonpath']
            log.info("Loading the data")
            df = pd.read_csv(path)
            # db_cursor= sqlite3.connect('sqlite3.db')
            # create
            for index, row in df.iterrows():
                airline = row['airline']
                departure_time = row['departure_time']
                stops = row['stops']
                arrival_time = row['arrival_time']
                passenger_class = row['passenger_class']
                duration = row['duration']
                days_left = row['days_left']
                price = row['price']
                flight = Plane(
                    airline=airline,
                    departure_time=departure_time,
                    stops=stops,
                    arrival_time=arrival_time,
                    passenger_class=passenger_class,
                    duration=duration,
                    days_left=days_left,
                    price=price
                )
                flight.save()
                print(f"Plane: {airline}, {passenger_class} saved...")
                log.info("Data loaded successfully")
        except Exception as error:
            log.error(str(error))





