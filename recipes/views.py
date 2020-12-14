from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe
from django.views.generic import ListView

class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
