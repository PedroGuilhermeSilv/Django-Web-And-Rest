from django.urls import reverse, resolve
from recipe import views
from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_template_correct(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipe/pages/home.html')

    def test_recipe_home_template_show_not_found_where_is_not_recipe(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No results to show',
                      response.content.decode('utf-8'))

    def test_recipe_home_template_loads_recipes(self):
        # é possível passar author e category porém tem que ser enviado como dicionário # noqa: E501
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        response_context_recipe = response.context['recipes']
        response_content = response.content.decode('utf-8')

        # # verificando se foi adicionado apenas 1.
        self.assertEquals(len(response_context_recipe), 1)

        # Verificando se o conteúdo está sendo renderizado no HTML
        self.assertIn('Recipe title', response_content)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertEqual(view.func, views.category)

    def test_recipe_category_view_return_status_404_if_no_recipes(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 100000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_return_status_404_if_no_recipes(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000000}))
        self.assertEqual(response.status_code, 404)
