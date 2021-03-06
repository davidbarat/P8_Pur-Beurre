from django.test import TestCase
from search.models import Product, Category
from django.contrib.auth.models import User

# Create your tests here.


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.category_name = "Fromages"
        Category.objects.create(category_name=cls.category_name)
        # cat.save()
        cls.category = Category.objects.get(id=1)
        Product.objects.create(
            category=cls.category,
            product_id="10",
            barcode="00000010",
            product_name="test",
            resume="test",
            picture_path="na",
            small_picture_path="na",
            nutriscore_grade="na",
            url="na",
        )

        User.objects.create(
            email="test@test.te",
            password="test123",
            first_name="Test",
            last_name="test",
            username="Tester",
        )

    def test_first_name_label(self):
        product = Product.objects.get(category_id=1)
        field_label = product._meta.get_field("product_name").verbose_name
        self.assertEquals(field_label, "product name")

    def test_get_absolute_url(self):
        product = Product.objects.get(product_id=10)
        self.assertEquals(product.get_absolute_url(), "/search/myproducts/10/")

    def test_product_name_max_length(self):
        product = Product.objects.get(product_id=10)
        max_length = product._meta.get_field("product_name").max_length
        self.assertEquals(max_length, 100)
