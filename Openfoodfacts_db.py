#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql.cursors
from openfoodfacts_url import openfoodfacts_categories()

def db_connection():
    """
    Connect to the database
    """
    connexion = pymysql.connect(host='localhost',
                                user='root',
                                password='jojo',
                                db='Projet_5_Openfoodfacts',)
    return connexion

def db_create_table_categories():

    """CREATE TABLE Categories (
    id_categorie INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
)
ENGINE=InnoDB;   """

def db_create_table_produits():

    """CREATE TABLE Produits (
    id_produit VARCHAR(13) PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    marque VARCHAR(40),
    grade CHAR(1),
    url VARCHAR(100),
    id_categorie INT,
    CONSTRAINT fk_id_categorie
        FOREIGN KEY (id_categorie)
        REFERENCES Categories(id_categorie)
)
ENGINE=InnoDB;
"""
#def db_update_table_categories():
    """
    maj des données dans la table Categories
    """

#def db_update_table_produits():
    """
    maj des données dans la table Produits
    """
