from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def test_url_recipe_home_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_url_recipe_category_is_correct(self):
        category_url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(category_url, '/recipes/category/1/')

    def test_url_recipe_detail_is_correct(self):
        recipe_url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(recipe_url, '/recipe/1/')
