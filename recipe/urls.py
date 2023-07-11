from django.urls import path
from recipe.views import home


urlpatterns = [
    path('', home)
]
