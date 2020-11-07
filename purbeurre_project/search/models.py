from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend, UserModel
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category,
        on_delete=models.DO_NOTHING
    )
    product_id = models.AutoField(primary_key=True)
    barcode = models.BigIntegerField()
    product_name = models.CharField(
        max_length=100, default="na", primary_key = False)
    resume = models.CharField(max_length=1000)
    picture_path = models.URLField()
    small_picture_path = models.URLField()
    nutriscore_grade = models.CharField(max_length=2)
    url = models.URLField()


class DetailProduct(models.Model):

    id = models.OneToOneField(
        Product, 
        to_field="product_id", 
        primary_key = True, 
        on_delete = models.CASCADE)
    energy_100g = models.DecimalField(max_digits=7, decimal_places=2)
    energy_unit = models.CharField(max_length=5)
    proteins_100g = models.DecimalField(max_digits=6, decimal_places=2)
    fat_100g = models.DecimalField(max_digits=6, decimal_places=2)
    saturated_fat_100g = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates_100g = models.DecimalField(max_digits=6, decimal_places=2)
    sugars_100g = models.DecimalField(max_digits=6, decimal_places=2)
    fiber_100g = models.DecimalField(max_digits=6, decimal_places=2)
    salt_100g = models.DecimalField(max_digits=6, decimal_places=2)


class Substitute(models.Model):

    id = models.AutoField(primary_key=True)
    user_email = models.EmailField(
        max_length=50, default='dav.barat@gmail.com')
    substitute_id = models.ForeignKey(
        Product, to_field="product_id", on_delete=models.CASCADE)


class EmailBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(email__iexact=username))   
        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None