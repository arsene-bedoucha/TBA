Arsène BEDOUCHA

Abdourrahman MOKEDDEM

Cellule Maudite
===============

Un jeu d’aventure en mode texte dans une prison , rempli de pièces lugubres, d’objets à récupérer, de PNJ à écouter et de quêtes à terminer pour espérer t’en sortir vivant.

Guide Utilisateur
-----------------

### Description

Bienvenue dans Cellule Maudite. Le jeu se lance dans le terminal et tu joues uniquement avec des commandes. Tu explores les salles, tu ramasses des objets, tu parles à des personnages et tu complètes des quêtes pour gagner des points.

Ton but est simple : Sortir de la prison.

Mais si tu atteins la sortie sans être prêt tu perds.

Univers
-------

Le jeu se déroule dans une prison abandonnée. Voici toutes les pièces présentes dans le jeu :

Salle Principale  
Cuisine  
Parloir  
Infirmerie  
Accueil  
Réserve  
EscaliersHaut  
EscaliersBas  
Cellule  
Ma cellule  
Sortie

plan : regarder dans le dossier image.

Personnages non joueur
----------------------

Dans certaines pièces, tu peux parler à des personnages :

Guardien : un personnage lié à une quête, il te donne une interaction importante pour avancer et gagner des points  
Sage : un personnage qui te guide et sert pour une quête spécifique à valider  
Prisonnier : un personnage à qui tu dois parler pour débloquer une quête et progresser dans le jeu

Conditions de Victoire
----------------------

Pour gagner, tu dois :

Atteindre la pièce Sortie  
Avoir un score total supérieur ou égal à 150 points

Les points se gagnent uniquement en complétant des quêtes.

Si tu as 150 points ou plus au moment d’arriver à la sortie, tu gagnes.

Conditions de Défaite
---------------------

Tu perds si :

Tu arrives dans la pièce Sortie  
Mais ton score total est inférieur à 150 points

Le jeu considère que tu n’étais pas assez prêt, la prison se referme sur toi, et c’est fini.

Objets
------

Voici les objets présents dans le jeu et à quoi ils servent :

Clé : sert à valider une quête liée à la progression et permet d’avancer vers la sortie  
Plan : sert à compléter une quête et aide à “réussir l’exploration” du jeu  
Medicament : sert à compléter une quête liée à l'infirmerie  
Livre : sert à valider une quête liée à un objet spécifique à récupérer  
Panier : sert à compléter une quête d’objet à trouver  
Coffre : objet important dans le jeu, lié à une quête où tu dois l’ouvrir
Téléphone : sert dans une quête.

Quêtes
------

Le jeu possède plusieurs quêtes qui te permettent de gagner des points.Certaines sont basées sur l’exploration, d’autres sur la collecte d’objets, et d’autres sur l’interaction avec les PNJ.

Voici toutes les quêtes disponibles dans le jeu :

OuvrirCoffre : terminer l’objectif lié au coffre, et récupérer ce qu’il contient  
Explorateur : avancer dans la prison et visiter les lieux importants  
Visiteur : aller dans une pièce spécifique pour valider une étape d’exploration  
LePlan : récupérer le plan pour compléter la quête et gagner des points  
LesMédocs : récupérer les médicaments dans l’infirmerie  
LaClé : obtenir la clé qui sert à progresser et valider une étape importante  
LeLivre : trouver le livre et compléter la quête associée  
LePanier : récupérer le panier et valider la quête  
LePrisonnier : parler au prisonnier pour compléter cette quête  
LeGuardien : parler au gardien pour compléter cette quête   
NourrireSage : interaction liée au sage, à faire pour compléter la quête

Tu peux voir leur progression avec la commande quests et leurs détails avec quest.

Installation
------------

Clone le dépôt GitHub :  
git clone https://github.com/arsene-bedoucha/TBA

Lance le jeu :  
python ./game.py

Commandes
---------

help : affiche la liste des commandes disponibles  
quit : quitte le jeu  
go : se déplacer dans une direction (N, E, S, O, Up, Down)  
history : affiche l'historique des pièces visitées  
back : revenir dans la pièce précédente  
look : regarder ce qu'il y a dans la pièce actuelle  
take : prendre un objet dans la pièce  
drop : déposer un objet dans la pièce  
check : afficher ton inventaire  
talk : parler à un PNJ dans la pièce  
quests : afficher la liste des quêtes  
quest : afficher les détails d’une quête  
activate : activer une quête  
rewards : afficher les récompenses obtenues  
points : afficher ton score  
activate\_all\_quests : activer toutes les quêtes d’un coup

Guide Developpeur
-----------------

### Diagramme de classes : regarder le fichier dans les images.

Perspectives de Développement
-----------------------------

Vidéo disponible sur GitHub mais aussi avec le lien suivant.
Lien vidéo : https://drive.google.com/file/d/1tYDEz3AsKdFBmGGflkRaQpybt4Gn2AvL/view?usp=drive_link
Note Pylint : 9,1/10.

Voici quelques améliorations qu’on aurait pu ajouter à Cellule Maudite.

### PNJ

Plus de dialogues  
Des dialogues à choix  
Des réactions selon l’inventaire ou les quêtes

### Quêtes

Ajouter des quêtes secondaires  
Ajouter des quêtes avec plusieurs choix possibles

### Gameplay

Ajouter des objets utilisables  
Ajouter des salles/événements supplémentaires

### Bon jeu ! 