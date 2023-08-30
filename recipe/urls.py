from django.urls import path
from recipe import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/',
         views.category, name="category"),
    path('recipe/<int:id>/', views.recipe, name="recipe"),
]
