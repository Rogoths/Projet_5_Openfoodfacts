#!/usr/bin/python3
# -*- coding: utf-8 -*
#import json
import requests

from Openfoodfacts_db import db_connection, insert_categories_db, insert_products_db,insert_product_db
from openfoodfacts_objects import Product

def openfoodfacts_categories():
    """
    Liste categories
    """

    url = requests.get("https://fr.openfoodfacts.org/langue/francais/categories.json")
    data_raw = url.json()
    data_categories = data_raw["tags"]
    for categories in data_categories[0:10]:
        name_cat = (categories["name"])

        insert_categories_db(name_cat)

def openfoodfacts_produits(cat_id):
    nb_page = 1
    while nb_page <= 40/40:
        url = requests.get("https://fr.openfoodfacts.org/langue/francais/categorie/"+str(cat_id)+"/"+str(nb_page)+".json")#page 2

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

                prod_dict[id_prod] = name_prod, brand_prod, grade_prod

            except Exception as e:
                print(e)

        for prod_id, prod in prod_dict.items():
            name, brand, grade = prod

            try:
                print(prod_id, name, brand, grade)
                insert_products_db(prod_id, name, brand, grade)
            except Exception as e:
                print(e)

def openfoodfacts_produit(product_id):
    url_prod = "https://fr.openfoodfacts.org/api/v0/product/"+str(product_id)
    url = requests.get(url_prod+".json")
    data_raw = url.json()

    data_produit = data_raw["product"]
    print(product_id)
        #product = Product()
    nom = data_produit["product_name"]
    marque = data_produit["brands"]
    grade = data_produit["nutrition_grades"]

    insert_product_db(product_id, marque, grade)
        #product.url = "https://fr.openfoodfacts.org/produit/"+str(product_id)+str(product.nom)



"""
def insert_produits_db(id_prod, name_prod):

    curs, con_db = db_connection() #tuples
    curs.execute(
        "INSERT produits VALUES (%s, %s)", id_prod, name_prod
    )
    con_db.commit()
"""
if __name__ == '__main__':
    openfoodfacts_produits()
