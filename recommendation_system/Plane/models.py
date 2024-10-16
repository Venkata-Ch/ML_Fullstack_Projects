from django.db import models


class Plane(models.Model):
    airline = models.CharField(max_length=20,null=False)
    departure_time = models.CharField(max_length=30, null=False)
    stops = models.CharField(max_length=10,null=False)
    arrival_time = models.CharField(max_length=6,null=False)
    passenger_class = models.CharField(max_length=10,null=False)
    duration = models.FloatField(null=False)
    days_left = models.IntegerField(null=False)
    price = models.FloatField(max_length=6,null=False)
    recommend = models.BooleanField(default=False)

