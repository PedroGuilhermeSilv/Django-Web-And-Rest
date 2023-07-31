from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=145)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipe/covers/%Y/%m/%d/',blank=True,default='')

    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.title
    ...