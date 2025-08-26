"""Define URL patterns for meal_plans."""
from django.urls import path
from . import views

app_name = "meal_plans"
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page to view all the meals
    path('meals/', views.meals, name='meals'),
    # Page to view individual food
    path('meal/<int: meal_id>/', views.meal, name='meal'),
]
