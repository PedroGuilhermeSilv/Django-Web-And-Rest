from django.contrib import admin
from recipe.models import Category
from recipe.models import Recipe

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...

class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category,CategoryAdmin)
admin.site.register(Recipe,RecipeAdmin)