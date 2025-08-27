from django.shortcuts import render     # render the response based on data provided by views
from .models import Meal

# Create your views here.
def index(request):
    """The home page of the meal_plans app"""
    return render(request, 'meal_plans/index.html')

def meals(request):
    """Page to show all available meals"""
    meals = Meal.objects.all()
    context = {'meals': meals}
    return render(request, 'meal_plans/meals.html', context)

def meal(request, meal_id):
    """Page to show an individual meal"""
    meal = Meal.objects.get(id=meal_id)
    meal_items = meal.mealitem_set.all()    # reverse lookup <modelname>_set.
    context = {'meal': meal, 'meal_items': meal_items}
    return render(request, 'meal_plans/meal.html', context)

