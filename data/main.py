import json
from database import api

list_categories = [
            'Snacks',
            'Boissons',
            'Produits Laitiers',
            'Produits à tartiner',
            'Fromages']
list_db = []
dir_export_json = "/Users/david/OpenClassrooms/P8/P8_Pur-Beurre/purbeurre_project/search/fixtures"

my_api = api()
list_product = []

for idx, category in enumerate(list_categories, 1):
    # list_product = my_api.get_info_from_api(category, idx)
    list_product.append(my_api.get_info_from_api(category, idx))

# print(list_product)

counter = 1
data = {}
fields = {}
for idx, element in enumerate(list_product):
    # print(element)
    # print('\n')
    for unique in element:
        print(unique)
        print('\n')
        data['model'] = "search.products"
        data['pk'] = None
        fields['barcode'] = unique[0]
        fields['categories'] = unique[1]
        fields['product_name'] = unique[2]
        fields['resume'] = unique[3]
        fields['nutriscore_grade'] = unique[4]
        fields['picture_path'] = unique[5]
        counter += 1 
        # list_db.append(fields)
        data['fields'] = fields
        list_db.append(data)
        data = {}
        fields = {}


# print(list_db)

with open(dir_export_json + '/export_data.json', 'w', encoding='utf-8') as f:
    json.dump(list_db, f, ensure_ascii=False, indent=4)
