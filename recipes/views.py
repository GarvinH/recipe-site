from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

recipes = [
    {
        'title': 'Cake',
        'author': 'Garvin',
        'date': 'December 11 2020',
        'prepTime': '30 minutes',
        'cookTime': '5 minutes'
    },
    {
        'title': 'Pizza',
        'author': 'Garvin',
        'date': 'December 11 2020',
        'prepTime': '60 minutes',
        'cookTime': '20 minutes'
    }
]

def recipe(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, "recipes/recipes.html", context)

