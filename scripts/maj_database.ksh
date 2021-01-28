#!/bin/sh 

cd /home/david
. django/bin/activate

for products in `cat /home/david/log/not-found-products.log | awk -F: '{ print $2}' | uniq` 
do
    echo $products
    python3 ./maj_database.py $products
done
