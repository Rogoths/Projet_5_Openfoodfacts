#!/usr/bin/python3
# -*- coding: utf-8 -*
from openfoodfacts_url import openfoodfacts_categories, openfoodfacts_produits
from Openfoodfacts_db import  create_db, db_create_table_categories, db_create_table_produits, show_categories_db, select_categories_db, del_products_table, del_categories_table, select_substitute, show_products_db

def display_choice():
    """ diplay choices for the user """
    print("1 Trouver un aliment dans la base de données")
    print("2 Suppression des tables")

    #return display_selection


def select_choice():
    """ input for the first selection """
    user_answer = int(input(":"))

    return user_answer

def category_choice():
    """ input for the category selection """

    user_answer = int(input("Quelle catégorie choisissez-vous?"))
    return user_answer

def product_choice():
    """ input for the product selection """
    user_answer = int(input("Quelle produit choisissez-vous?"))

def main_screen():
    """ main method """

    try:
        create_db()
    except:
        print("Base de données déjà existante")
    try:
        db_create_table_categories()
    except:
        print("Table Categories déjà existante")
    try:
        db_create_table_produits()
    except:
        print("Table Produits déjà existante")

    openfoodfacts_categories()

    first_screen = True


    while first_screen:
        del_screen = False
        selection_screen = False
        display_choice()
        main_answer = select_choice()
        print(main_answer)
        first_screen = False
    if main_answer == 1:
        selection_screen = True

        while selection_screen:
            show_categories_db()
            answer = category_choice()
            cat_select = select_categories_db(answer)
            openfoodfacts_produits(cat_select)
            selection_screen = False
            substitut_screen = True

            while substitut_screen:
                show_products_db()
                product_answer = product_choice()
                select_substitute(answer)





    elif main_answer == 2:
        del_screen = True
        while del_screen:

            del_products_table()
            del_categories_table()
            print("retour au menu principal")
            del_screen = False
            first_screen = True


    else:
        print("Veuillez entrer un chiffre valide")


main_screen()
