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
        "CREATE DATABASE IF NOT EXISTS Projet_5_Openfoodfacts CHARACTER SET 'utf8';"
    )
    print("Création de la base de données - Projet_5_Openfoodfacts -")
    con_db.commit()

def db_create_table_categories():

    curs, con_db = db_connection()

    curs.execute(
        "CREATE TABLE IF NOT EXISTS Categories ("
        "id_categorie INT AUTO_INCREMENT,"
        "nom VARCHAR(100) NOT NULL,"
        "PRIMARY KEY(id_categorie))"
    )
    con_db.commit()
    print("Création de la table - catégories -")

def db_create_table_produits():

    curs, con_db = db_connection()

    curs.execute(
        "CREATE TABLE IF NOT EXISTS Produits ("
        "id_produit VARCHAR(13) PRIMARY KEY,"
        "nom VARCHAR(100) NOT NULL,"
        "marque VARCHAR(40),"
        "grade CHAR(1),"
        "substitut_id CHAR(100),"
        "url VARCHAR(100),"
        "id_categorie INT,"
        "FOREIGN KEY (id_categorie) REFERENCES Categories(id_categorie))"
    )
    con_db.commit()
    print("Création de la table - produits -")

def insert_categories_db(name_cat):

    curs, con_db = db_connection() #tuples
    curs.execute(
        "INSERT categories VALUES (NULL, %s)",name_cat
    )
    con_db.commit()


def show_categories_db():

    curs, con_db = db_connection()

    curs.execute(
        "CREATE TABLE IF NOT EXISTS Produits ("
        "id_produit VARCHAR(13) PRIMARY KEY,"
        "nom VARCHAR(100) NOT NULL,"
        "marque VARCHAR(40),"
        "grade CHAR(1),"
        "substitut_id CHAR(100),"
        "url VARCHAR(100),"
        "id_categorie INT,"
        "FOREIGN KEY (id_categorie) REFERENCES Categories(id_categorie))"
    )
    con_db.commit()
    print("affichage des catégories -")

"""
def select_substitute(id_categorie):

    curs, con_db = db_connection()

    curs.execute(
        "SELECT id_produit, nom, marque, grade, url FROM Produits WHERE id_categorie = %s AND grade = "a"", id_categorie
        )
"""
