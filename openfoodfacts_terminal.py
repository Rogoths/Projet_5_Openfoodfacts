#!/usr/bin/python3
# -*- coding: utf-8 -*
from openfoodfacts_url import openfoodfacts_categories, openfoodfacts_produits, openfoodfacts_produit
from Openfoodfacts_db import  create_db, db_create_table_categories, db_create_table_produits, show_categories_db, select_categories_db, del_products_table, del_categories_table, show_products_db, select_product_db, show_user_selection, insert_substituts_db, db_create_table_subtituts, del_substituts_table, insert_substituts_db

def display_choice():
    """ diplay choices for the user """
    print("-"*50)
    print("MENU PRINCIPAL")
    print("-"*50)
    print("1 Trouver un aliment dans la base de données")
    print("2 Suppression des tables")

    #return display_selection

def select_choice():
    """ input for the first selection """
    user_answer = int(input(":"))

    return user_answer

def category_choice(data):
    """ input for the category selection """
    print("-"*50)
    print("CHOIX DE LA CATEGORIE")
    print("-"*50)

    user_answer = input("Quelle catégorie choisissez-vous?")

    liste_ids = [ str(elem[0]) for elem in data ]#convert element in string

    while user_answer not in liste_ids:
        print("id inexistant - Veuillez reessayer")
        user_answer = input("Quelle catégorie choisissez-vous?")

    return user_answer

def product_choice(data):
    """ input for the product selection """
    print("-"*50)
    print("CHOIX DU PRODUIT")
    print("-"*50)
    user_answer = input("Quelle produit choisissez-vous?")

    liste_ids = [ str(elem[0]) for elem in data ]

    while user_answer not in liste_ids:
        print("id inexistant - Veuillez reessayer")
        user_answer = input("Quelle produit choisissez-vous?")

    return user_answer

def substitut_choice():
    """ input for the substitut selection """
    print("-"*50)
    print("MENU SUBSTITUT")
    print("-"*50)
    user_answer = int(input("Que voulez-vous faire? \n 1-Revenir au menu principal \n 2-Sauvegarder un substitut?"))

    return user_answer

def substitut_saved_choice(data):
    """ input for the substitut to save selection """
    print("-"*50)
    print("MENU SAVE SUBSTITUT")
    print("-"*50)
    user_answer = str(input("Entrez le code substitut : "))
    liste_ids = [ elem[0] for elem in data ]

    while user_answer not in liste_ids:
        print("id inexistant - Veuillez reessayer")
        user_answer = str(input("Entrez le code substitut : "))

    return user_answer

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

    #openfoodfacts_categories()

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
                data_cat = show_categories_db()
                answer = category_choice(data_cat)
                cat_select = select_categories_db(answer)

                openfoodfacts_produits(cat_select)

                    #print("-----------")
                selection_screen = False
                product_screen = True

                while product_screen:
                    data_prod = show_products_db()
                    product_answer = product_choice(data_prod)
                    prod_select = show_user_selection(product_answer)
                    product_screen = False
                    substitut_screen = True

                    while substitut_screen:
                        substitut_answer = substitut_choice()


                        if substitut_answer == 1:
                            first_screen = True
                        elif substitut_answer == 2:

                            substitut_save_screen = True
                            while substitut_save_screen:
                                print(prod_select)
                                sub_answer = substitut_saved_choice(prod_select)
                                insert_substituts_db(sub_answer)
                        else:
                            substitut_screen = False
                            continue









        elif main_answer == 2:
            del_screen = True
            while del_screen:
                try:
                    del_substituts_table()
                except:
                    print("Table Substituts déjà supprimée -")
                try:
                    del_products_table()
                except:
                    print("Table Produits déjà supprimée -")
                try:
                    del_categories_table()
                except:
                    print("Table Categories déjà supprimée -")

                try:

                    db_create_table_categories()
                except:
                    print("table Categorie déjà existante -")
                try:
                    db_create_table_produits()
                except:
                    print("table Produit déjà existante -")
                try:
                    db_create_table_subtituts()
                except:
                    print("table substituts déjà existante -")
                print("retour au menu principal")
                openfoodfacts_categories()
                del_screen = False
                first_screen = True
                continue


        else:
            print("Veuillez entrer un chiffre valide")


main_screen()
