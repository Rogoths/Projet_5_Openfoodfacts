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
    limit_categories = 0
    for categories in data_categories:
        if limit_categories < 10:
            name = str(categories["name"])
            insert_categories_db(name)
            limit_categories += 1

def insert_categories_db(name):

    con_db = db_connection()
    con_db.query(
        "INSERT INTO categories"
        "VALUES (NULL, '{0}')".format(name)
    )
"""
def openfoodfacts_produits(categorie):

    url = requests.get("https://fr.openfoodfacts.org/langue/francais/categorie/"+str(categorie)".json")
    data_raw = url.json()
    data_produits = data_raw["products"]
    dict_produits = {}
    for produits in data_produits:
        dict_produits.append(produits["product_name_fr"])


    for id_produit in data_produits
"""

openfoodfacts_categories()
