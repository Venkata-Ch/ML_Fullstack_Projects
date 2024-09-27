from django.urls import path
from . import views


urlpatterns = [
    path('templates/index.html', view=views.flight_recommendation),
]

