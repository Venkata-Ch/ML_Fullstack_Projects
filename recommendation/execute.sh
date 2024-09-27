#!/bin/bash
python manage.py data_load --pythonpath flights_data.csv &&
python manage.py make_recommendations &&
python manage.py runserver 0.0.0.0:8000
