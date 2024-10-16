from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from urllib3 import request
import sqlite3
from .models import Plane
from . import views
# Create your views here.

# class Fli_View:
#     def __init__(self):
#         pass



def home(request):
    return render(request, 'home.html')

def flight_recommendation(request):
    if request.method == "GET":
        description = fli_data()
        return render(request,'index.html',description)


def fli_data():
    description = {}
    recommended_fl_count = Plane.objects.filter(stops="one").count()

    if recommended_fl_count !=0:
        flights = Plane.objects.filter(stops="one").order_by('-price')[:20]
    else:
        flights = Plane.objects.filter(passenger_class='Economy').order_by('-price')[:20]
    description['flights_list'] = flights

    return description



def recommend(request):
    if request.method == "GET":
        description = recommended_flights()
        return render(request,'recommended_flights.html',description)

def recommended_flights():
    recommended = {}
    recommended_fl_count = Plane.objects.filter(recommend=True).count()

    if recommended_fl_count !=0:
        flights = Plane.objects.filter(stops="one").order_by('-price')[:20]
    else:
        flights = Plane.objects.filter(passenger_class='Economy').order_by('-price')[:20]
    recommended['recommended_list'] = flights

    return recommended

# def main():
#     fi = Fli_View()
#     fi.flight_recommendation()
#
# if __name__=="__main__":
#     main()



