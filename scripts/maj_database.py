from django.core.management.base import BaseCommand
from search.models import Product, Category, DetailProduct
from django.db import IntegrityError 
from django.core.exceptions import MultipleObjectsReturned
from logging.handlers import RotatingFileHandler
from logging import handlers
from configparser import ConfigParser
import requests
import logging

parser = ConfigParser() 
parser.read('/home/david/conf/configuration.ini')
path = parser.get('settings', 'log_path_majdb')

logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.DEBUG)
    
handler = RotatingFileHandler(
        path + 'majdb.log',
        maxBytes=2000, 
        backupCount=5)
logger.addHandler(handler)

def __init__(self):
    # api-endpoint
    self.list_product = []
    self.url = "https://fr.openfoodfacts.org/cgi/search.pl"

def populate(self, list_product):
    for self.category in self.list_categories:
        cat, _ = Category.objects.get_or_create(category_name=self.category)
        cat.save()
    print(list_product[0])
    print(list_product[-4:])

    for self.element in list_product:
        # print(self.element)
        logger.info(self.element)
        logger.info(self.element[0])
        # print(self.element[0])
        # for self.unique in self.element:
        category = Category.objects.get(id=self.element[1])
        try:  
            product, created = Product.objects.get_or_create(
                    barcode=self.element[0],
                    product_name=self.element[2],
                    resume=self.element[3],
                    nutriscore_grade=self.element[4],
                    picture_path=self.element[5],
                    url=self.element[6],
                    small_picture_path=self.element[7],
                    category=category,
                )  
            if created:
                product.save()
        except IntegrityError: 
            print(IntegrityError)
        except MultipleObjectsReturned:
            print(MultipleObjectsReturned)
        except Exception as e:
            raise e

        try:
            detail_product, created = DetailProduct.objects.get_or_create(
                    id=product,
                    energy_100g=self.element[8],
                    energy_unit=self.element[9],
                    proteins_100g=self.element[10],
                    fat_100g=self.element[11],
                    saturated_fat_100g=self.element[12],
                    carbohydrates_100g=self.element[13],
                    sugars_100g=self.element[14],
                    fiber_100g=self.element[15],
                    salt_100g=self.element[16],
                )
            if created:
                detail_product.save()
        except IntegrityError:
            print(IntegrityError)
        except MultipleObjectsReturned:
            print(MultipleObjectsReturned)
        except Exception as e:
            raise e

def handle(self, *args, **options):
    for self.idx, self.category in enumerate(self.list_categories, 1):
        self.payload = {
            "tag_0": "categories",
            "tag_contains_0": "contains",
            "tagtype_0": "categories",
            "sort_by": "unique_scans_n",
            "page": 1,
            "page_size": 20,
            "action": "process",
            "json": 1,
        }
        print("Get Data from Api Category :" + " " + self.category)
        logger.info("Get Data from Api Category :" + " " + self.category)

        for c in range(1, 6, 1):  # 5 pages
            self.payload["page"] = c
            self.payload["tag_0"] = self.category
            for j in range(1, 19, 1):  #  20 resultats par pages
                self.r = requests.get(
                    url=self.url,
                    params=self.payload,
                    headers={
                        "UserAgent": "Project OpenFood - MacOS - Version 10.13.6"
                    },
                )
                self.data = self.r.json()

                if not "nutriscore_grade" in self.data["products"][j]:
                    self.data["products"][j]["nutriscore_grade"] = "na"
                if not "ingredients_text_fr" in self.data["products"][j]:
                    self.data["products"][j]["ingredients_text_fr"] = "na"
                if not "image_url" in self.data["products"][j]:
                    self.data["products"][j]["image_url"] = "na"
                if not "image_small_url" in self.data["products"][j]:
                    self.data["products"][j]["image_small_url"] = "na"
                if not "url" in self.data["products"][j]:
                    self.data["products"][j]["url"] = "na"
                if not "energy_100g" in self.data["products"][j]["nutriments"]:
                    self.data["products"][j]["nutriments"]["energy_100g"] = "00"
                if not "energy_unit" in self.data["products"][j]["nutriments"]:
                    self.data["products"][j]["nutriments"]["energy_unit"] = "na"
                if not "proteins_100g" in self.data["products"][j]["nutriments"]:
                    self.data["products"][j]["nutriments"]["proteins_100g"] = "00"
                if not "fat_100g" in self.data["products"][j]["nutriments"]:
                    self.data["products"][j]["nutriments"]["fat_100g"] = "00"
                if (
                    not "saturated_fat_100g"
                    in self.data["products"][j]["nutriments"]
                ):
                    self.data["products"][j]["nutriments"][
                        "saturated_fat_100g"
                    ] = "00"
                if (
                    not "carbohydrates_100g"
                    in self.data["products"][j]["nutriments"]
                ):
                    self.data["products"][j]["nutriments"][
                        "carbohydrates_100g"
                    ] = "00"
                if not "sugars_100g" in self.data["products"][j]["nutriments"]:
                    self.data["products"][j]["nutriments"]["sugars_100g"] = "00"
                if not "fiber_100g" in self.data["products"][j]["nutriments"]:
                    self.data["products"][j]["nutriments"]["fiber_100g"] = "00"
                if not "salt_100g" in self.data["products"][j]["nutriments"]:
                    self.data["products"][j]["nutriments"]["salt_100g"] = "00"

                self.list_product.append(
                    (
                        self.data["products"][j]["code"],
                        self.idx,
                        self.data["products"][j]["product_name"],
                        self.data["products"][j]["ingredients_text_fr"],
                        self.data["products"][j]["nutriscore_grade"],
                        self.data["products"][j]["image_url"],
                        self.data["products"][j]["url"],
                        self.data["products"][j]["image_small_url"],
                        self.data["products"][j]["nutriments"]["energy_100g"],
                        self.data["products"][j]["nutriments"]["energy_unit"],
                        self.data["products"][j]["nutriments"]["proteins_100g"],
                        self.data["products"][j]["nutriments"]["fat_100g"],
                        self.data["products"][j]["nutriments"][
                            "saturated_fat_100g"
                        ],
                        self.data["products"][j]["nutriments"][
                            "carbohydrates_100g"
                        ],
                        self.data["products"][j]["nutriments"]["sugars_100g"],
                        self.data["products"][j]["nutriments"]["fiber_100g"],
                        self.data["products"][j]["nutriments"]["salt_100g"],
                    )
                )

    self.populate(self.list_product)
