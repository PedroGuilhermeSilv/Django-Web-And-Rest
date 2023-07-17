from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render
from utils.recipe.factory import make_recipe

def home(request):
    return render(request,'recipe/pages/home.html',context={
    'recipes':[make_recipe() for _ in range(10)],
    })

def recipe(request,id):
    return render(request,'recipe/pages/recipe-view.html',context={
    'recipe':make_recipe(),'is_details_page':True,
    })

