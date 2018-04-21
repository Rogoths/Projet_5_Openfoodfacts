#!/usr/bin/python3
# -*- coding: utf-8 -*
from openfoodfacts_url import openfoodfacts_categories, openfoodfacts_produits


def display_choice():
    """ diplay choices for the user """
    display_selection = print("1 Trouver un aliment dans la base de données")

    return display_selection

def select_choice():
    """ input for the first selection """
    user_answer = input(":")

    return user_answer

def category_choice():
    """ input for the category selection """
    openfoodfacts_categories()
    user_answer = input("Quelle catégorie choisissez-vous?")
    return user_answer

def product_choice():
    """ input for the product selection """
    user_answer = input("Quelle produit choisissez-vous?")

def main_screen():
    """ main method """
    display_choice()
    answer = select_choice()
    if answer == "1":
        category_name = category_choice()
        openfoodfacts_produits(category_name)

    else:
        print("Veuillez entrer un chiffre valide")
        main_screen()

main_screen()
