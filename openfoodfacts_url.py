#!/usr/bin/python3
# -*- coding: utf-8 -*
#import json
import requests
from openfoodfacts_db import db_connection

def openfoodfacts_categories():
    """
    Liste categories
    """

    url = requests.get("https://fr.openfoodfacts.org/langue/francais/categories.json")
    data_raw = url.json()
    data_categories = data_raw["tags"]
    for categories in data_categories[0:10]:
        name_cat = str(categories["name"])
        print(name_cat)
        insert_categories_db(name_cat)

def insert_categories_db(name_cat):

    curs, con_db = db_connection() #tuples
    curs.execute(
        "INSERT categories VALUES (NULL, %s)",name_cat
    )
    con_db.commit()

def openfoodfacts_produits():

    url = requests.get("https://fr.openfoodfacts.org/langue/francais/categorie/boissons.json")
    data_raw = url.json()
    data_produits = data_raw["products"]
    for produits in data_produits:
        name_prod = str(produits["product_name_fr"])
        id_prod = str(produits["_id"])
        print(id_prod, name_prod)
        insert_produits_db(id_prod, name_prod)

def insert_produits_db(id_prod, name_prod):

    curs, con_db = db_connection() #tuples
    curs.execute(
        "INSERT produits VALUES (%s, %s)", id_prod, name_prod
    )
    con_db.commit()



openfoodfacts_produits()
