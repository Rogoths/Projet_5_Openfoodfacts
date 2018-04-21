#!/usr/bin/python3
# -*- coding: utf-8 -*
#import json
import requests
from openfoodfacts_db import db_connection, insert_categories_db
from openfoodfacts_objects import Product

def openfoodfacts_categories():
    """
    Liste categories
    """

    url = requests.get("https://fr.openfoodfacts.org/langue/francais/categories.json")
    data_raw = url.json()
    data_categories = data_raw["tags"]
    for categories in data_categories[0:15]:
        name_cat = str(categories["name"])
        print(name_cat)
        insert_categories_db(name_cat)

def openfoodfacts_produits():

    url = requests.get("https://fr.openfoodfacts.org/langue/francais/categorie/pizzas/2.json")
    data_raw = url.json()
    data_produits = data_raw["products"]
    prod_dict = {}
    #list_id = []
    for produits in data_produits:
        name_prod = str(produits["product_name"])
        id_prod = str(produits["_id"])
        try:
            prod_dict[id_prod] = name_prod #dict for products with id
        except KeyError:
            print("keyerror!")
    for prod_id, prod in prod_dict.items():
        #list_id.append(id) #use it for the product url
        print(prod_id, prod)
    #insert_produits_db(id_prod, name_prod)

def openfoodfacts_produit(product_id):

    url = requests.get("https://fr.openfoodfacts.org/api/v0/product/"+str(id_product)+".json")
    data_raw = url.json()
    data_produit = data_raw["product"]
    product = Product()
    product.nom = data_produit["product_name"]
    product.marque = data_produit["brands"]
    product.grade = data_produit["nutrition_grades"]
    #product.url = "https://fr.openfoodfacts.org/produit/"+str(product_id)+str(product.nom)
    print(product.nom, product.marque, product.grade)


"""
def insert_produits_db(id_prod, name_prod):

    curs, con_db = db_connection() #tuples
    curs.execute(
        "INSERT produits VALUES (%s, %s)", id_prod, name_prod
    )
    con_db.commit()
"""

openfoodfacts_categories()
