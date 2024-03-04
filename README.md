# Projet Apprentissage Automatique - Analyse des Joueurs de la NBA 2020
Ce projet propose une approche d'apprentissage automatique pour prédire le poste d'un joueur de basketball de la NBA en fonction de ses caractéristiques physiques. L'algorithme des k-plus proches voisins est utilisé pour cette tâche.
# Contenu du Projet
## Introduction

Le projet vise à prédire le poste (Centre, Ailier, Arrière/Meneur de jeu) des joueurs de la NBA en 2020 en fonction de leurs caractéristiques physiques.
## Chargement des Données

Les données des joueurs de la NBA en 2020 sont chargées à partir du fichier CSV "joueursNBA2020.csv" en utilisant les bibliothèques Python pandas et numpy.
## Filtrage des Données par Poste

Les joueurs sont filtrés en fonction de leur poste, créant des DataFrames distincts pour chaque catégorie.
## Visualisation sur un Graphique

Une fonction points est utilisée pour afficher un graphique montrant les joueurs en fonction de leur taille et poids, distingués par leur poste.
## Prédiction du Poste des Joueurs Polyvalents

Identification et prédiction du poste des joueurs polyvalents ('G-F') en utilisant l'algorithme des k-plus proches voisins.
Algorithme des k-plus Proches Voisins

Construction de DataFrames pour chaque poste ('G', 'F', 'C') et création d'un DataFrame global.
Calcul de la distance entre un joueur inconnu et les joueurs des différents postes.
Mise en œuvre de l'algorithme des k-plus proches voisins pour prédire le poste probable d'un joueur.
# Utilisation du Code
Environnement de Développement

Le code est écrit en langage Python et utilise les bibliothèques pandas, numpy, et matplotlib.
Assurez-vous d'avoir un environnement Python configuré avec ces dépendances.
Exécution du Code

Exécutez le script Python projet_apprentissage_automatique.py pour obtenir les résultats.
Assurez-vous que le fichier de données "joueursNBA2020.csv" est présent dans le même répertoire.
Visualisation des Graphiques

Les graphiques affichent la répartition des joueurs en fonction de leur taille et poids, ainsi que la prédiction pour un joueur spécifique.
