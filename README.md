# Projet_5_Openfoodfacts
<h1>Projet n°5 : Utilisez les données publiques de l'OpenFoodFacts</h1>

<h2>Installation :</h2>

Dans votre console :
<li>pip install -r requirements.txt</li>


<h2>I - Menu Principal, sélectionner l'un des choix indiqué par un chiffre :</h2>

   <li>1 - Trouver un aliment dans la base de données
    Récupération dans L'API Open Food Facts des catégories
    Insertion des données dans la base de données</li>
   <li>2 - Suppression des tables
    Suppression des tables dans la base de données</li>
   <li>3 - Afficher les produits substituts sauvegardés
    Sélection dans la base de données de la table Substituts</li>

<h2>II - Sélection par l'utilisateur d'une catégorie :</h2>
    Récupération dans L'API Open Food Facts des produits de la catégorie
    Insertion des données dans la base de données

<h2>III - Sélection par l'utilisateur d'un produit :</h2>
    Affichage des données produit et de ses substituts via la base de données

<h2>IV - Enregistrement (ou non) d'un substitut à ce produit :</h2>
    Enregistrement dans la base de données des substituts

<h2>PARAMETRAGE :</h2>

Fichier openfoodfacts_url.py

ligne 9 à 11
<li>NB_PROD_PAGE = 20 #nombre de produit par page qui peut changer</li>
<li>NB_PROD_REQUEST = 60 #nombre de produit souhaité par le développeur</li>
<li>NB_CAT_REQUEST = 20 #nombre de catégorie souhaité par le développeur</li>
