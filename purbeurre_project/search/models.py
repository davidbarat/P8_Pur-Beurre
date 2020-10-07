from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, default='David')
    email = models.EmailField(max_length=50, default='dav.barat@gmail.com')
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD = 'username'


class Product(models.Model):
    category = models.ForeignKey(Category,
        on_delete=models.DO_NOTHING
    )
    barcode = models.BigIntegerField()
    product_name = models.CharField(max_length=100, default="na")
    resume = models.CharField(max_length=1000)
    picture_path = models.URLField()
    nutriscore_grade = models.CharField(max_length=2)


class Substitute(models.Model):
    products_barcode = models.OneToOneField(
        Product,
        primary_key=True,
        on_delete=models.DO_NOTHING
    )
    products_selected = models.CharField(max_length=20)