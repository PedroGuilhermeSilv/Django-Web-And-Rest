from django.contrib import admin
from recipe.models import Category
from recipe.models import Recipe

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category,CategoryAdmin)
