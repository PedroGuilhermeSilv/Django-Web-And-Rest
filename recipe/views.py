from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render
from utils.recipe.factory import make_recipe
from recipe.models import Recipe

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request,'recipe/pages/home.html',context={
    'recipes':recipes
    })

def category(request,category_id):
    recipes = Recipe.objects.filter(category__id = category_id,is_published=True).order_by('-id')
    return render(request,'recipe/pages/home.html',context={
    'recipes':recipes
    })

def recipe(request,id):
    return render(request,'recipe/pages/recipe-view.html',context={
    'recipe':make_recipe(),'is_details_page':True,
    })

