from django.db import models

# Create your models here.

class Categories(models.Model):
    category_name = models.CharField(max_length=30)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=50)


class Products(models.Model):
    categories = models.OneToOneField(
        Categories,
        on_delete=models.DO_NOTHING
    )
    resume = models.CharField(max_length=200)
    picture_path = models.URLField()
    nutriscore_grade = models.CharField(max_length=1)


class Substitute(models.Model):
    products_barcode = models.OneToOneField(
        Products,
        primary_key=True,
        on_delete=models.DO_NOTHING
    )
    products_selected = models.CharField(max_length=20)