#!/usr/bin/python3
# -*- coding: utf-8 -*
#import json
import requests

from Openfoodfacts_db import db_connection, insert_categories_db, insert_products_db
from openfoodfacts_objects import Product

def openfoodfacts_categories():
    """
    read the categories from open food facts api and select some categorie
    """

    url = requests.get("https://fr.openfoodfacts.org/langue/francais/categories.json")
    data_raw = url.json()
    data_categories = data_raw["tags"]
    for categories in data_categories[0:10]:
        name_cat = (categories["name"])

        insert_categories_db(name_cat)

def openfoodfacts_produits(cat_id):
    """read open food facts api and select id name brand grade detail
    from a selected categorie"""
    nb_page = 1
    while nb_page <= 40/20:
        url = requests.get("https://fr.openfoodfacts.org/langue/francais/categorie/"+str(cat_id)+"/"+str(nb_page)+".json")

        data_raw = url.json()
        data_produits = data_raw["products"]
        prod_dict = {}
        #list_id = []
        #product_number = 0
        nb_page = nb_page +1
        for produits in data_produits:

            try:
                name_prod = (produits["product_name"])
                id_prod = (produits["_id"])
                brand_prod = (produits["brands"])
                grade_prod = (produits["nutrition_grades"])
                detail_prod = (produits["generic_name_fr"])
                stores_prod = (produits["stores"])
                url_prod = "https://fr.openfoodfacts.org/produit/"+str(produits["_id"])
                cat_prod = cat_id[0][0]

                prod_dict[id_prod] = name_prod, brand_prod, grade_prod, detail_prod, stores_prod, url_prod, cat_prod

            except Exception as e:
                pass

        for prod_id, prod in prod_dict.items():
            name, brand, grade, detail, stores, url, cat = prod

            try:
                #print(prod_id, name, brand, grade, detail, url, cat)
                insert_products_db(prod_id, name, brand, grade, detail, stores, url, cat)

            except Exception as e:
                print(e)

if __name__ == '__main__':
    openfoodfacts_produits("barres")
