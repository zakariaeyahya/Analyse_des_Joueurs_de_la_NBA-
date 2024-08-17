<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        img {
            max-width: 100%;
            height: auto;
            margin-bottom: 20px;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        ul {
            padding-left: 20px;
        }
    </style>
</head>
<body>
<img src="https://github.com/user-attachments/assets/f932607a-51cd-4f00-9962-6170ae5039c2" alt="Image du projet">

<h1>Projet Apprentissage Automatique - Analyse des Joueurs de la NBA 2020</h1>

<p>
    <a href="mailto:zakariae.yh@gmail.com">zakariae.yh@gmail.com</a> |
    <a href="https://www.linkedin.com/in/zakariae-yahya">www.linkedin.com/in/zakariae-yahya</a>
</p>

<h2>Technologies utilisées</h2>
<p>
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
    <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
    <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
    <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
</p>

<p>Ce projet propose une approche d'apprentissage automatique pour prédire le poste d'un joueur de basketball de la NBA en fonction de ses caractéristiques physiques. L'algorithme des k-plus proches voisins est utilisé pour cette tâche.</p>

<h2>Contenu du Projet</h2>

<h3>Introduction</h3>
<p>Le projet vise à prédire le poste (Centre, Ailier, Arrière/Meneur de jeu) des joueurs de la NBA en 2020 en fonction de leurs caractéristiques physiques.</p>

<h3>Chargement des Données</h3>
<p>Les données des joueurs de la NBA en 2020 sont chargées à partir du fichier CSV "joueursNBA2020.csv" en utilisant les bibliothèques Python pandas et numpy.</p>

<h3>Filtrage des Données par Poste</h3>
<p>Les joueurs sont filtrés en fonction de leur poste, créant des DataFrames distincts pour chaque catégorie.</p>

<h3>Visualisation sur un Graphique</h3>
<p>Une fonction points est utilisée pour afficher un graphique montrant les joueurs en fonction de leur taille et poids, distingués par leur poste.</p>

<img src="https://github.com/zakariaeyahya/Analyse_des_Joueurs_de_la_NBA-/assets/155691167/98078744-a251-46dd-a68b-9048b76a8198" alt="Graphique 1">
<img src="https://github.com/zakariaeyahya/Analyse_des_Joueurs_de_la_NBA-/assets/155691167/61eadfd1-b658-4996-a28b-94bf4dee027e" alt="Graphique 2">
<img src="https://github.com/zakariaeyahya/Analyse_des_Joueurs_de_la_NBA-/assets/155691167/47b9bd72-45a9-4787-9aa0-ecb87c945e40" alt="Graphique 3">
<img src="https://github.com/zakariaeyahya/Analyse_des_Joueurs_de_la_NBA-/assets/155691167/58776a1e-3eb6-4624-b384-ecf0c516fca7" alt="Graphique 4">

<h3>Prédiction du Poste des Joueurs Polyvalents</h3>
<p>Identification et prédiction du poste des joueurs polyvalents ('G-F') en utilisant l'algorithme des k-plus proches voisins.</p>

<h3>Algorithme des k-plus Proches Voisins</h3>
<ul>
    <li>Construction de DataFrames pour chaque poste ('G', 'F', 'C') et création d'un DataFrame global.</li>
    <li>Calcul de la distance entre un joueur inconnu et les joueurs des différents postes.</li>
    <li>Mise en œuvre de l'algorithme des k-plus proches voisins pour prédire le poste probable d'un joueur.</li>
</ul>

<img src="https://github.com/zakariaeyahya/Analyse_des_Joueurs_de_la_NBA-/assets/155691167/bdd3b03e-42ce-416b-924b-cd5c9bc666c3" alt="Graphique KNN">

<h2>Utilisation du Code</h2>

<h3>Environnement de Développement</h3>
<p>Le code est écrit en langage Python et utilise les bibliothèques pandas, numpy, et matplotlib.</p>

<h3>Bibliothèques utilisées</h3>
<pre><code>
 numpy 
 pandas 
 matplotlib.pyplot 
</code></pre>

<h3>Jeu de données</h3>
<p>Le jeu de données est disponible sur <a href="https://github.com/zakariaeyahya/Analyse_des_Joueurs_de_la_NBA-/blob/main/joueursNBA2020.csv">GitHub</a>.</p>

</body>
</html>
