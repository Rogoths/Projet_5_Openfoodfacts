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
                                db='Projet_5_Openfoodfacts',)
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
        "substitut_id CHAR(100),"
        "url VARCHAR(100),"
        "id_categorie INT,"
        "PRIMARY KEY (id_produit),"
        "FOREIGN KEY (id_categorie) REFERENCES Categories(id_categorie));"
    )
    con_db.commit()
    print("Création de la table - produits -")

def insert_categories_db(name_cat):

    curs, con_db = db_connection() #tuples
    curs.execute(
        "INSERT INTO Categories VALUES (NULL, %s)",name_cat
    )
    con_db.commit()


def show_categories_db():

    curs, con_db = db_connection()

    curs.execute(
        "SELECT id_categorie, nom FROM Categories"
    )
    data = curs.fetchall()
    con_db.commit()

    print("affichage des catégories -")
    print(data)

def select_categories_db(cat_choice):

    curs, con_db = db_connection()

    curs.execute(
        "SELECT nom FROM Categories WHERE id_categorie=%s",cat_choice
    )
    data = curs.fetchall()
    con_db.commit()
    return data

def insert_products_db(id_prod, name_prod):
    curs, con_db = db_connection() #tuples
    curs.execute(
        "INSERT INTO Produits VALUES (NULL, '%d', '%s', NULL, NULL, NULL, NULL, NULL)"#,id_prod, name_prod#use the two parameters
    )
    data = curs.fetchall()
    con_db.commit()

def show_products_db():

    curs, con_db = db_connection()

    curs.execute(
        "SELECT id_produit, nom FROM Produits"
    )
    data = curs.fetchall()
    con_db.commit()
    print("affichage des produits -")
    print(data)

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

def select_substitute(id_categorie):

    curs, con_db = db_connection()

    curs.execute(
        "SELECT id_produit, ean_produit, nom, marque, grade, url FROM Produits WHERE id_categorie='%s' AND grade ='a'"
    )
    data = curs.fetchall()
    con_db.commit()

    print("affichage substituts -")
    return data
