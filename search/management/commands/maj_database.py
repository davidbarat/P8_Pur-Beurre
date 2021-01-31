from django.core.management.base import BaseCommand
from search.models import Product, Category, DetailProduct
from django.db import IntegrityError 
from django.core.exceptions import MultipleObjectsReturned
from logging.handlers import RotatingFileHandler
from logging import handlers
from configparser import ConfigParser
import requests
import logging
import sys

"""
parser = ConfigParser() 
parser.read('/home/david/conf/configuration.ini')
path = parser.get('settings', 'log_path')
"""
class Command(BaseCommand):
    help = "Populate DB from log file not_found-product"

    def __init__(self):
        # api-endpoint
        self.product = []
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"

    def populate(self, product, category):
        category = Category.objects.get(id=product[0][1])
        try:  
            product_maj, created = Product.objects.get_or_create(
                    barcode=product[0][0],
                    product_name=product[0][2],
                    resume=product[0][3],
                    nutriscore_grade=product[0][4],
                    picture_path=product[0][5],
                    url=product[0][6],
                    small_picture_path=product[0][7],
                    category=category,
                )  
            if created:
                product_maj.save()
        except IntegrityError: 
            print(IntegrityError)
        except MultipleObjectsReturned:
            print(MultipleObjectsReturned)
        except Exception as e:
            raise e
        try:
            print(product)
            self.idx_product = Product.objects.get(product_name=product[0][2])
            print(self.idx_product)
            print(self.idx_product.product_id)
            self.index = Product.objects.get(product_id=self.idx_product.product_id)
            detail_product, created = DetailProduct.objects.get_or_create(
                    id=self.index,
                    energy_100g=product[0][8],
                    energy_unit=product[0][9],
                    proteins_100g=product[0][10],
                    fat_100g=product[0][11],
                    saturated_fat_100g=product[0][12],
                    carbohydrates_100g=product[0][13],
                    sugars_100g=product[0][14],
                    fiber_100g=product[0][15],
                    salt_100g=product[0][16],
                )
            if created:
                detail_product.save()
        except IntegrityError:
            print(IntegrityError)
        except MultipleObjectsReturned:
            print(MultipleObjectsReturned)
        except Exception as e:
            raise e

    def add_arguments(self, parser):
        parser.add_argument('search', type=str)

    def handle(self, *args, **options):

        self.search = options['search']
        self.payload = {
            "search_terms2": self.search,
            "limit": 1,
            "page": 1,
            "skip": 0,
            "action": "process",
            "json": 1,
        }
        print("Get Data from Api")
        self.r = requests.get(
            url=self.url,
            params=self.payload,
            headers={
                "UserAgent": "Project OpenFood - MacOS - Version 10.13.6"
            },
        )
        self.data = self.r.json()
        if not "nutriscore_grade" in self.data["products"][0]:
            self.data["products"][0]["nutriscore_grade"] = "na"
        if not "ingredients_text_fr" in self.data["products"][0]:
            self.data["products"][0]["ingredients_text_fr"] = "na"
        if not "image_url" in self.data["products"][0]:
            self.data["products"][0]["image_url"] = "na"
        if not "image_small_url" in self.data["products"][0]:
            self.data["products"][0]["image_small_url"] = "na"
        if not "url" in self.data["products"][0]:
            self.data["products"][0]["url"] = "na"
        if not "energy_100g" in self.data["products"][0]["nutriments"]:
            self.data["products"][0]["nutriments"]["energy_100g"] = "00"
        if not "energy_unit" in self.data["products"][0]["nutriments"]:
            self.data["products"][0]["nutriments"]["energy_unit"] = "na"
        if not "proteins_100g" in self.data["products"][0]["nutriments"]:
            self.data["products"][0]["nutriments"]["proteins_100g"] = "00"
        if not "fat_100g" in self.data["products"][0]["nutriments"]:
            self.data["products"][0]["nutriments"]["fat_100g"] = "00"
        if (
            not "saturated_fat_100g"
            in self.data["products"][0]["nutriments"]
        ):
            self.data["products"][0]["nutriments"][
                "saturated_fat_100g"
            ] = "00"
        if (
            not "carbohydrates_100g"
            in self.data["products"][0]["nutriments"]
        ):
            self.data["products"][0]["nutriments"][
                "carbohydrates_100g"
            ] = "00"
        if not "sugars_100g" in self.data["products"][0]["nutriments"]:
            self.data["products"][0]["nutriments"]["sugars_100g"] = "00"
        if not "fiber_100g" in self.data["products"][0]["nutriments"]:
            self.data["products"][0]["nutriments"]["fiber_100g"] = "00"
        if not "salt_100g" in self.data["products"][0]["nutriments"]:
            self.data["products"][0]["nutriments"]["salt_100g"] = "00"

        
        category = self.data["products"][0]["categories"].split(",")
        print(category)
        cat, _ = Category.objects.get_or_create(category_name=category[0])
        cat.save()
        self.idx_category = Category.objects.get(category_name=cat)
        print(self.idx_category.id)

        self.product.append(
            (
                self.data["products"][0]["code"],
                self.idx_category.id,
                self.data["products"][0]["product_name"],
                self.data["products"][0]["ingredients_text_fr"],
                self.data["products"][0]["nutriscore_grade"],
                self.data["products"][0]["image_url"],
                self.data["products"][0]["url"],
                self.data["products"][0]["image_small_url"],
                self.data["products"][0]["nutriments"]["energy_100g"],
                self.data["products"][0]["nutriments"]["energy_unit"],
                self.data["products"][0]["nutriments"]["proteins_100g"],
                self.data["products"][0]["nutriments"]["fat_100g"],
                self.data["products"][0]["nutriments"][
                    "saturated_fat_100g"
                ],
                self.data["products"][0]["nutriments"][
                    "carbohydrates_100g"
                ],
                self.data["products"][0]["nutriments"]["sugars_100g"],
                self.data["products"][0]["nutriments"]["fiber_100g"],
                self.data["products"][0]["nutriments"]["salt_100g"],
            )
        )
        self.populate(self.product, self.idx_category.id)
