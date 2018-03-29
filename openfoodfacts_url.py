#!/env/bin/python3
# -*- coding: utf-8 -*
#import json
import requests
from openfoodfacts_db import *
def openfoodfacts_categories():
    """
    Liste categories
    """

    url = requests.get("https://fr.openfoodfacts.org/langue/francais/categories.json")
    data_raw = url.json()
    data_categories = data_raw["tags"]
    limit_categories = 0
    liste_categories = []
    for categories in data_categories:
        if limit_categories < 10:
            liste_categories.append(categories["name"])
            limit_categories += 1

            print(liste_categories)

def openfoodfacts_produits(categorie):
    """
    liste Produits
    """
    url = requests.get("https://fr.openfoodfacts.org/langue/francais/categorie/"+str(categorie)".json")
    data_raw = url.json()
    data_produits = data_raw["products"]
    dict_produits = {}
    for produits in data_produits:
        dict_produits.append(produits["product_name_fr"])


    for id_produit in data_produits


def openfoodfacts_produit():
    """
    Détails produit
    """
    url = requests.get("https://fr.openfoodfacts.org/api/v0/produit/"+str(id_produit)".json")
    data_raw = url.json()
    data_produit =
"""
