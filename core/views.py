from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from .models import *

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def get_recipe(dish_name = None):
    if dish_name:
        recipes = Recipe.objects.filter(recipe_name__contains = dish_name)
    else:
        recipes = Recipe.objects.all()
    return recipes
    
def home(request):
    context = {}
    query = request.GET.get("query")
    if cache.get(query):
        recipes = cache.get(query)
        print("####################DATA COMING FROM CACHE####################")
    else:
        if query:
            recipes = get_recipe(query)
            cache.set(query, recipes)
            print("####################CACHE SET####################")
        else:
            recipes = get_recipe()
        print("####################DATA NOT COMING FROM CACHE####################")
            
    context['recipes'] = recipes[:12]
    return render(request, 'home.html', context)

def view_recipe(request, pk):
    context = {}
    if cache.get(pk):
        recipe = cache.get(pk)
        print("####################DATA COMING FROM CACHE####################")
    else:
        recipe = Recipe.objects.get(pk = pk)
        cache.set(pk, recipe)
        print("####################CACHE SET####################")
        print("####################DATA NOT COMING FROM CACHE####################")
    
    context['recipe'] = recipe
    
    recipes = get_recipe()[:10]
    context['recipes'] = recipes
    
    return render(request, 'view_recipe.html', context)