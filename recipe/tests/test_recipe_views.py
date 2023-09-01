from django.test import TestCase
from django.urls import reverse, resolve
from recipe import views
from recipe.models import Category, User, Recipe


class RecipeViewsTest(TestCase):
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
        # category = Category.objects.create(name='Categoria')
        category = Category(name='Categoria')
        category.save()

        author = User.objects.create_user(
            first_name='name',
            username='user',
            email='user@email',
            password='123456'
        )
        recipe = Recipe.objects.create(
            author=author,
            category=category,
            title='Recipe title',
            description='description at recipe',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe preparation steps',
            preparation_steps_is_html=False,
            is_published=True
        )
        response = self.client.get(reverse('recipes:home'))
        response_context_recipe = response.context['recipes']
        response_content = response.content.decode('utf-8')
        # # verificando se foi adicionado apenas 1.
        self.assertEquals(len(response_context_recipe), 1)

        # # Verificando se o titulo adicionado é igual ao que foi enviado
        self.assertEquals(
            response_context_recipe.first().title, 'Recipe title')

        # Verificando se o conteúdo está sendo renderizado no HTML
        self.assertIn('Recipe title', response_content)
        self.assertIn('10 Minutos', response_content)
        self.assertIn('5 Porções', response_content)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIn(view.func, views.category)

    def test_recipe_category_view_return_status_404_if_no_recipes(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 100000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_return_status_404_if_no_recipes(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 404)
