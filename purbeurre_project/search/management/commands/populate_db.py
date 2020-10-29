from django.core.management.base import BaseCommand
from search.models import Product, Category
import requests


class Command(BaseCommand):
    help = 'Populate DB from api Open Food Facts'

    def __init__(self):
        # api-endpoint 
        self.list_product = []
        self.list_categories = [
            'Snacks',
            'Boissons',
            'Produits Laitiers',
            'Produits à tartiner',
            'Fromages']
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl"

    def populate(self, list_product):

        for self.category in self.list_categories:
            cat, _ = Category.objects.get_or_create(category_name=self.category)
            cat.save()
        print(list_product[0])
        print(list_product[-4:])

        for self.element in list_product:
            print(self.element)
            print(self.element[0])
            # for self.unique in self.element:
            category = Category.objects.get(id=self.element[1])
            product, _  = Product.objects.get_or_create(
                barcode=self.element[0],
                product_name = self.element[2],
                resume = self.element[3],
                nutriscore_grade = self.element[4],
                picture_path = self.element[5],
                url = self.element[6],
                small_picture_path = self.element[7],
                category = category
            )
            """ product.product_name = self.element[2]
            product.resume = self.element[3]
            product.nutriscore_grade = self.element[4]
            product.picture_path = self.element[5]
            product.category = self.element[1] """
            product.save()
                
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
                "json": 1
            }
            print(
                    'Get Data from Api Category :'
                    + ' ' + self.category
                    )

            for c in range(1,6,1): # 5 pages
                self.payload['page'] = c
                self.payload['tag_0'] = self.category
                for j in range(1, 19, 1): #  20 resultats par pages
                    self.r = requests.get(
                        url = self.url,
                        params = self.payload,
                        headers = {
                            'UserAgent':
                            'Project OpenFood - MacOS - Version 10.13.6'
                            }
                    )
                    self.data = self.r.json()
    
                    if not 'nutriscore_grade' in self.data['products'][j]:
                        self.data['products'][j]['nutriscore_grade'] = 'na'
                    if not 'ingredients_text_fr' in self.data['products'][j]:
                        self.data['products'][j]['ingredients_text_fr'] = 'na'
                    if not 'image_url' in self.data['products'][j]:
                        self.data['products'][j]['image_url'] = 'na'
                    if not 'image_small_url' in self.data['products'][j]:
                        self.data['products'][j]['image_small_url'] = 'na'
                    if not 'url' in self.data['products'][j]:
                        self.data['products'][j]['url'] = 'na'
                    self.list_product.append(
                        (self.data['products'][j]['code'],
                        self.idx,
                        self.data['products'][j]['product_name'],
                        self.data['products'][j]['ingredients_text_fr'],
                        self.data['products'][j]['nutriscore_grade'],
                        self.data['products'][j]['image_url'],
                        self.data['products'][j]['url'],
                        self.data['products'][j]['image_small_url']
                        )
                    )

        self.populate(self.list_product)