#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql.cursors
#import records


def db_connection():#select_substitute(answer)

    """
    Connect to the database
    """

    connexion = pymysql.connect(host='localhost',
                                user='root',
                                password='jojo',
                                db='Projet_5_Openfoodfacts',
                                charset='utf8')
    curs = connexion.cursor()
    return curs, connexion


def create_db():
    curs, con_db = db_connection()

    curs.execute(
        "CREATE DATABASE Projet_5_Openfoodfacts CHARACTER SET 'utf8';"
    )
    print("Création de la base de données - Projet_5_Openfoodfacts -")
    con_db.commit()

def db_create_table_categories():

    curs, con_db = db_connection()

    curs.execute(
        "CREATE TABLE Categories ("
        "id_categorie INT AUTO_INCREMENT,"
        "nom VARCHAR(100) NOT NULL,"
        "UNIQUE (nom),"
        "PRIMARY KEY(id_categorie));"
    )
    con_db.commit()
    print("Création de la table - catégories -")

def db_create_table_produits():

    curs, con_db = db_connection()

    curs.execute(
        "CREATE TABLE Produits ("
        "id_produit INT AUTO_INCREMENT,"
        "ean_produit VARCHAR(13),"
        "nom VARCHAR(100) NOT NULL,"
        "marque VARCHAR(40),"
        "grade CHAR(1),"
        "details VARCHAR(100),"
        "url VARCHAR(100),"
        "substitut_id CHAR(100),"
        "categorie VARCHAR(100),"
        "UNIQUE KEY (ean_produit),"
        "PRIMARY KEY (id_produit),"
        "CONSTRAINT fk_categorie_nom FOREIGN KEY (categorie) REFERENCES Categories(nom));"
    )
    con_db.commit()
    print("Création de la table - produits -")

def db_create_table_subtituts():

    curs, con_db = db_connection()

    curs.execute(
        "CREATE TABLE Substituts ("
        "id_substitut INT AUTO_INCREMENT,"
        "nom VARCHAR(100) NOT NULL,"
        "UNIQUE (nom),"
        "PRIMARY KEY(id_substitut));"
    )
    con_db.commit()
    print("Création de la table - substituts -")

def insert_substituts_db(name_sub):
    curs, con_db = db_connection() #tuples
    try:
        curs.execute(
            "INSERT INTO Substituts (nom) SELECT nom FROM Produits WHERE id_produit=%s",name_sub
        )
    except Exception as e:
        print(e)
    con_db.commit()


def insert_categories_db(name_cat):

    curs, con_db = db_connection() #tuples
    try:
        curs.execute(
            "INSERT INTO Categories VALUES (NULL, %s) ON DUPLICATE KEY UPDATE id_categorie=NULL",name_cat
        )
    except Exception as e:
        print(e)
    con_db.commit()


def show_categories_db():

    curs, con_db = db_connection()

    curs.execute(
        "SELECT id_categorie, nom FROM Categories"
    )
    data = curs.fetchall()
    con_db.commit()

    print("affichage des catégories -")
    print("-"*50)
    for line in data:
        print(str(line[0])+"-"+line[1])

    return data

def select_categories_db(cat_choice):

    curs, con_db = db_connection()

    curs.execute(
        "SELECT nom FROM Categories WHERE id_categorie=%s",cat_choice
    )
    data = curs.fetchall()
    con_db.commit()
    return data

def select_product_db(prod_choice):

    curs, con_db = db_connection()

    curs.execute(
        "SELECT nom FROM Categories WHERE id_categorie=%s",prod_choice
    )
    data = curs.fetchall()
    con_db.commit()
    return data

def insert_products_db(id_prod, name_prod, brand_prod, grade_prod, detail_prod, url_prod, cat_prod):
    product_var = id_prod, name_prod, brand_prod, grade_prod, detail_prod, url_prod, cat_prod, name_prod
    curs, con_db = db_connection() #tuples
    try:
        curs.execute(
            "INSERT INTO Produits VALUES (NULL, %s, %s, %s, %s, %s, %s, NULL, %s) ON DUPLICATE KEY UPDATE nom=%s",product_var#use the two parameters
        )
    except Warning:
        pass
    con_db.commit()

def insert_product_db(product_id, brand_prod, grade):

    product_var = brand_prod, grade, product_id
    curs, con_db = db_connection() #tuples
    try:
        curs.execute(
            "UPDATE Produits SET marque=%s, grade=%s WHERE ean_produit=%s",product_var
        )
    except Exception as e:
        print(e)
    data = curs.fetchall()
    con_db.commit()
    #print(data)


def show_products_db():

    curs, con_db = db_connection()

    curs.execute(
        "SELECT id_produit, ean_produit, nom, grade FROM Produits"
    )
    data = curs.fetchall()
    con_db.commit()
    print("affichage des produits -")
    print("-"*50)

    for line in data:
        print(str(line[0])+"-"+line[2])

    return data

def del_substituts_table():
    curs, con_db = db_connection() #tuples
    curs.execute(
        "DROP TABLE Substituts;"
    )
    con_db.commit()

def del_products_table():
    curs, con_db = db_connection() #tuples
    curs.execute(
        "DROP TABLE Produits;"
    )
    con_db.commit()

def del_categories_table():
    curs, con_db = db_connection() #tuples
    curs.execute(
        "DROP TABLE Categories;"
    )
    con_db.commit()

def show_substituts(grade, categorie):
    selection = grade, categorie

    curs, con_db = db_connection()

    curs.execute(
        "SELECT id_produit, ean_produit, nom, marque, grade, details, url FROM Produits WHERE grade<=%s AND categorie=%s ORDER BY grade ASC LIMIT 5",selection
    )
    data = curs.fetchall()
    num_substitut = 1
    code_sub = []
    for line in data:

        code_sub.append(str(line[0]))
        print("substitut n°"+str(num_substitut)+" code "+str(line[0]))
        print("-"*50)
        print("\n-Nom : "+str(line[2])+"\n-Marque : "+str(line[3])+"\n-Nutriscore : "+str(line[4])+"\n-Description : "+str(line[5])+"\n-Lien : "+str(line[6]))
        print("-"*50)

        num_substitut += 1
    con_db.commit()

    return code_sub

def show_user_selection(selection):

    curs, con_db = db_connection()

    curs.execute(
        "SELECT id_produit, ean_produit, nom, marque, grade, categorie, details, url FROM Produits WHERE id_produit=%s",selection
    )
    data = curs.fetchall()

    print("affichage détails produits -")
    for line in data:
        grade = str(line[4])
        categorie = str(line[5])
        print("-"*50)
        print("\n-Nom : "+str(line[2])+"\n-Marque : "+str(line[3])+"\n-Nutriscore : "+str(line[4])+"\n-Description : "+str(line[5])+"\n-Lien : "+str(line[6]))
        print("-"*50)
        selection_substitut = show_substituts(grade, categorie)

    con_db.commit()

    return selection_substitut

if __name__ == '__main__':

    db_create_table_subtituts()
