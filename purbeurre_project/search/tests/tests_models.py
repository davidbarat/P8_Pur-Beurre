from django.test import TestCase
from search.models import Product, Category
from django.contrib.auth.models import User

# Create your tests here.

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(
            category = '1',
            product_id = '00000000',
            barcode = '00000000',
            product_name = 'test',
            resume = 'test',
            picture_path = 'na',
            small_picture_path = 'na',
            nutriscore_grade = 'na',
            url = 'na'
            )

    def test_first_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('product_name').verbose_name
        self.assertEquals(field_label, 'product name')

    """
    def test_date_of_death_label(self):
        author=Product.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        author = Product.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Product.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Product.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1')
 """