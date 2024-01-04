from django.test import TestCase
from recipe.models import Category, User, Recipe


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='cateogry_name'):
        return Category.objects.create(name=name)

    def make_author(self,
                    first_name='name',
                    username='user',
                    email='user@email',
                    password='123456'
                    ):
        return User.objects.create_user(
            first_name=first_name,
            username=username,
            email=email,
            password=password
        )

    def make_recipe(self,
                    author_data=None,
                    category_data=None,
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
                    ):

        if author_data is None:
            author_data = {}
        if category_data is None:
            category_data = {}
        return Recipe.objects.create(
            author=self.make_author(**author_data),
            category=self.make_category(**category_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published
        )
