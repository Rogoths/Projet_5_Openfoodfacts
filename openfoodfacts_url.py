#!/usr/bin/python3
# -*- coding: utf-8 -*
#import json
import requests
from Openfoodfacts_db import db_connection, insert_categories_db, insert_products_db
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

    url = requests.get("https://fr.openfoodfacts.org/langue/francais/categorie/"+str(cat_id)+"/2.json")#page 2
    data_raw = url.json()
    data_produits = data_raw["products"]
    prod_dict = {}
    #list_id = []
    #product_number = 0
    for produits in data_produits:
        name_prod = (produits["product_name"])
        id_prod = (produits["_id"])
        try:
            prod_dict[id_prod] = name_prod #dict for products with id
        except KeyError:
            print("keyerror!")
    for prod_id, prod in prod_dict.items():
        #list_id.append(id) #use it for the product url
        print(prod_id, prod)
        insert_products_db(prod_id, prod)

def openfoodfacts_produit(product_id):

    url = requests.get("https://fr.openfoodfacts.org/api/v0/product/"+str(product_id)+".json")
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
