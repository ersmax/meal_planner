from django.db import models

# Create your models here.
class Meal(models.Model):
    """A model for a single meal"""
    name = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """Return a string representing the meal"""
        return self.name
    
class MealItem(models.Model):
    """An item part of the meal"""
    name = models.CharField(max_length = 200)
    meal = models.ForeignKey(Meal, on_delete = models.CASCADE)  # Delete all food related with a delated meal
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Meal food'

    def __str__(self):
        """Return a string representing the specific food"""
        return self.name