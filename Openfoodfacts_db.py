#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql.cursors
#import records


def db_connection():

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
    """create the table categories in database"""

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
    """create the table Produits in database"""
    curs, con_db = db_connection()

    curs.execute(
        "CREATE TABLE Produits ("
        "id_produit INT AUTO_INCREMENT,"
        "ean_produit VARCHAR(13),"
        "nom VARCHAR(100) NOT NULL,"
        "marque VARCHAR(100),"
        "grade CHAR(1),"
        "details VARCHAR(200),"
        "magasins VARCHAR(200),"
        "url VARCHAR(100),"
        "categorie VARCHAR(100),"
        "UNIQUE KEY (ean_produit),"
        "PRIMARY KEY (id_produit),"
        "CONSTRAINT fk_categorie_nom FOREIGN KEY (categorie) REFERENCES Categories(nom));"
    )
    con_db.commit()
    print("Création de la table - produits -")

def db_create_table_subtituts():
    """create the table Substituts in database"""
    curs, con_db = db_connection()

    curs.execute(
        "CREATE TABLE Substituts ("
        "id_substitut INT NOT NULL,"
        "id_produit INT NOT NULL,"
        "CONSTRAINT fk_produit_id FOREIGN KEY (id_produit) REFERENCES Produits(id_produit));"
    )
    con_db.commit()
    print("Création de la table - substituts -")

def insert_substituts_db(id_sub, prod_sub):
    """Insert in database the substituts"""
    data_sub = id_sub, prod_sub
    curs, con_db = db_connection() #tuples

    curs.execute(
        "INSERT INTO Substituts (id_substitut, id_produit) VALUES (%s, %s)",data_sub
    )

    con_db.commit()


def insert_categories_db(name_cat):
    """insert categories in database"""
    curs, con_db = db_connection() #tuples
    try:
        curs.execute(
            "INSERT INTO Categories VALUES (NULL, %s) ON DUPLICATE KEY UPDATE id_categorie=NULL",name_cat
        )
    except Exception as e:
        print(e)
    con_db.commit()


def show_categories_db():
    """display the categories"""
    curs, con_db = db_connection()

    curs.execute(
        "SELECT id_categorie, nom FROM Categories ORDER BY id_categorie ASC"
    )
    data = curs.fetchall()
    con_db.commit()

    print("affichage des catégories -")
    print("-"*50)
    for line in data:
        print(str(line[0])+"-"+line[1])

    return data

def select_categories_db(cat_choice):
    """select the categories from user choice"""
    curs, con_db = db_connection()

    curs.execute(
        "SELECT nom FROM Categories WHERE id_categorie=%s",cat_choice
    )
    data = curs.fetchall()
    con_db.commit()
    return data

def insert_products_db(id_prod, name_prod, brand_prod, grade_prod, detail_prod, stores_prod, url_prod, cat_prod):
    """insert the product values in database"""
    product_var = id_prod, name_prod, brand_prod, grade_prod, detail_prod, stores_prod, url_prod, cat_prod, name_prod
    curs, con_db = db_connection() #tuples
    try:
        curs.execute(
            "INSERT INTO Produits VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE nom=%s",product_var
        )
    except Warning:
        pass
    con_db.commit()

def show_products_db(categorie):
    """display products from the selected categorie"""
    curs, con_db = db_connection()

    curs.execute(
        "SELECT id_produit, ean_produit, nom, grade FROM Produits WHERE categorie=%s", categorie
    )
    data = curs.fetchall()
    con_db.commit()
    print("affichage des produits -")
    print("-"*50)

    for line in data:
        print(str(line[0])+"-"+line[2])

    return data

def show_substituts_db():
    """display the product and the substituts informations from the table substituts"""
    curs, con_db = db_connection()

    curs.execute(
    """SELECT DISTINCT p1.id_produit, p1.ean_produit, p1.nom, p1.marque, p1.grade, p1.details, p1.magasins, p1.url,
    p2.id_produit, p2.ean_produit, p2.nom, p2.marque, p2.grade, p2.details, p2.magasins, p2.url
    FROM Substituts s LEFT JOIN Produits p1 ON p1.id_produit = s.id_produit LEFT JOIN Produits p2 ON p2.id_produit = s.id_substitut"""
    )

    data = curs.fetchall()
    con_db.commit()

    for rows in data:
        print("-"*50)
        print("-"*50)
        print("PRODUIT SUBSTITUÉ :")
        print("\n-Nom : "+str(rows[2])+"\n-Marque : "+str(rows[3])+"\n-Nutriscore : "+str(rows[4])+"\n-Description : "+str(rows[5])+"\n-Magasins : "+str(rows[6])+"\n-Lien : "+str(rows[7]))
        print("-"*50)
        print("SUBSTITUT DU PRODUIT :")
        print("\n-Nom : "+str(rows[10])+"\n-Marque : "+str(rows[11])+"\n-Nutriscore : "+str(rows[12])+"\n-Description : "+str(rows[13])+"\n-Magasins : "+str(rows[14])+"\n-Lien : "+str(rows[15]))
        print("-"*50)
        print("-"*50)

def del_substituts_table():
    """delete substituts table"""
    curs, con_db = db_connection() #tuples
    curs.execute(
        "DROP TABLE Substituts;"
    )
    con_db.commit()

def del_products_table():
    """delete products table"""
    curs, con_db = db_connection() #tuples
    curs.execute(
        "DROP TABLE Produits;"
    )
    con_db.commit()

def del_categories_table():
    """delete categories table"""
    curs, con_db = db_connection() #tuples
    curs.execute(
        "DROP TABLE Categories;"
    )
    con_db.commit()

def show_substituts(grade, categorie):
    """display the product and the substituts informations for the selected product"""
    selection = grade, categorie

    curs, con_db = db_connection()

    curs.execute(
        "SELECT id_produit, ean_produit, nom, marque, grade, details, magasins, url FROM Produits WHERE grade<=%s AND categorie=%s ORDER BY grade ASC LIMIT 5",selection
    )
    data = curs.fetchall()
    num_substitut = 1
    dict_sub = {}
    code_sub = []
    for line in data:

        code_sub = str(num_substitut)
        id_sub = str(line[0])
        dict_sub[code_sub] = id_sub
        print("substitut n°"+str(num_substitut)+" code "+str(line[0]))
        print("-"*50)
        print("\n-Nom : "+str(line[2])+"\n-Marque : "+str(line[3])+"\n-Nutriscore : "+str(line[4])+"\n-Description : "+str(line[5])+"\n-Magasins : "+str(line[6])+"\n-Lien : "+str(line[7]))
        print("-"*50)
        #print(dict_sub)
        num_substitut += 1
    con_db.commit()

    return dict_sub

def show_user_selection(selection):
    """show product details from the selected product"""
    curs, con_db = db_connection()

    curs.execute(
        "SELECT id_produit, ean_produit, nom, marque, grade, categorie, details, magasins, url FROM Produits WHERE id_produit=%s",selection
    )
    data = curs.fetchall()

    print("affichage détails produits -")
    for line in data:
        grade = str(line[4])
        categorie = str(line[5])
        print("-"*50)
        print("\n-Nom : "+str(line[2])+"\n-Marque : "+str(line[3])+"\n-Nutriscore : "+str(line[4])+"\n-Description : "+str(line[6])+"\n-Magasins : "+str(line[7])+"\n-Lien : "+str(line[8]))
        print("-"*50)
        selection_substitut = show_substituts(grade, categorie)

    con_db.commit()

    return selection_substitut

if __name__ == '__main__':

    show_substituts_db()
