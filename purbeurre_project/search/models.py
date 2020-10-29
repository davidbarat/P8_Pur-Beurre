from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend, UserModel
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Q


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name


""" class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, default='David')
    email = models.EmailField(max_length=50, default='dav.barat@gmail.com')
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD = 'username' """


class Product(models.Model):
    category = models.ForeignKey(Category,
        on_delete=models.DO_NOTHING
    )
    barcode = models.BigIntegerField()
    product_name = models.CharField(max_length=100, default="na")
    resume = models.CharField(max_length=1000)
    picture_path = models.URLField()
    small_picture_path = models.URLField()
    nutriscore_grade = models.CharField(max_length=2)
    url = models.URLField()



class Substitute(models.Model):
    products_barcode = models.OneToOneField(
        Product,
        primary_key=True,
        on_delete=models.DO_NOTHING
    )
    products_selected = models.CharField(max_length=20)


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(
                user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None