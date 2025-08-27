"""Defines URL patterns for meal_plans."""

from django.urls import path    # map URL to views

from . import views

app_name = 'meal_plans'         # distinguish urls.py of meal_plans app
urlpatterns = [                 # reachable URLs
    # Homepage: route to base URL, call index() from views.py, give name index
    path('', views.index, name='index'),
    # Page to view all meals.
    path('meals/', views.meals, name='meals'),
    # Page to view individual meals.
    path('meal/<int:meal_id>/', views.meal, name='meal'),
]
