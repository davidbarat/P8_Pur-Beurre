[![Build Status](https://travis-ci.com/davidbarat/P8_Pur-Beurre.svg?branch=master)](https://travis-ci.com/davidbarat/P8_Pur-Beurre)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# P8_Pur-Beurre
-------

The purpose of this project is to allow user to get healthy product instead of their usual fat products.

![alt text](https://github.com/davidbarat/P8_Pur-Beurre/blob/master/imagesite.png)

## Main steps of the script
1. The user has to fullfill the registration form,
2. Once connected, you can make a simple search, 
3. The site will return a list of product with a better nutriscore grade,
4. The user can have a detail view of the product and then if you mind, you can store your new fav product.
5. Finally the user can find all his new products in a myproducts link in the navbar at the top.

## class ApiGoogle
* def getKey:
	* get api google secret key
* def search_api_google:
	* do api call
  * get api response
  * create the dictionnary response


## Installing

Fork the project on your local machine and launch the script via these commands:

    pip install -r requirements.txt
    ./manage.py runserver

