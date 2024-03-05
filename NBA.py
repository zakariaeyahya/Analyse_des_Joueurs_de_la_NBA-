import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("joueursNBA2020.csv", sep=";")
tableau_reduit=data[['nom','equipe','poste','taille','poids','experience','pays']].dropna()
tableau_reduit['poids']=tableau_reduit['poids'].replace(to_replace ='kg',
value = '', regex = True)
tableau_reduit['poids']=tableau_reduit['poids'].astype('float')
tableau_reduit['taille']=tableau_reduit['taille'].astype('float')
print(tableau_reduit.head()) # on affiche le debut du tableau avec la
print(tableau_reduit.columns)
print(tableau_reduit.describe)
filtre = tableau_reduit['poste'] == 'C'
df = tableau_reduit[filtre]
print(df)
def plot_position_bar_chart():
    plt.figure(figsize=(8, 6))

    # Count the number of players in each position
    position_counts = tableau_reduit['poste'].value_counts()

    # Plot bar chart
    position_counts.plot(kind='bar', color=['blue', 'green', 'red'])
    
    plt.title('Number of Players in Each Position')
    plt.xlabel('Position')
    plt.ylabel('Number of Players')
    plt.xticks(rotation=0)
    plt.show()

# Function to plot line chart for player heights
def plot_height_line_chart():
    plt.figure(figsize=(10, 6))

    # Plot line chart for player heights
    plt.plot(tableau_reduit['taille'], marker='o', linestyle='-', color='purple')
  
    plt.title('Player Heights in NBA (2020)')
    plt.xlabel('Player Index')
    plt.ylabel('Height (meters)')
    plt.grid(True, linestyle='-', linewidth=0.5, color='red')
    plt.show()
def plot_weight_line_chart():
    plt.figure(figsize=(10, 6))

    # Plot line chart for player weights
    plt.plot(tableau_reduit['poids'], marker='o', linestyle='-', color='orange')

    plt.title('Player Weights in NBA (2020)')
    plt.xlabel('Player Index')
    plt.ylabel('Weight (kg)')
    plt.grid(True, linestyle='-', linewidth=0.5, color='red')
    plt.show()

plot_weight_line_chart()
plot_position_bar_chart()
plot_height_line_chart()

from matplotlib.patches import Ellipse, Circle
def points(postes, size=20, marker='o', alpha=0.5):
    for poste in postes:
        df = tableau_reduit[tableau_reduit['poste'] == poste]
        x = df['taille']
        y = df['poids']
        plt.scatter(x, y, label=poste, s=size, marker=marker, alpha=alpha)
plt.title('caractéristiques des joueurs de NBA 2020')
plt.xlabel("taille")
plt.ylabel("poids")
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
points('F')
points('G')
points('C',100,'D',1)
axes = plt.gca()
plt.legend()
plt.show()
plt.title('caractéristiques des joueurs de NBA 2020')
plt.xlabel("taille")
plt.ylabel("poids")
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
points('F')
axes = plt.gca()
plt.legend()
plt.show()

filtre = tableau_reduit['poste'] == 'G-F'
df_poly = tableau_reduit[filtre]
print(df_poly.head())
print(df_poly.iloc[0])
def joueur(num, rayon):
    ratio = 0.005 # echelle des X / echelle des Y
    plt.title('caractéristiques des joueurs de NBA 2020')
    plt.xlabel("taille")
    plt.ylabel("poids")
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    points(['F','G','C'])
    x = df_poly.loc[num]['taille']
    y = df_poly.loc[num]['poids']
    plt.scatter(x,y,s=50, marker='P', alpha=1)
    circle = plt.Circle((x, y), 1, color='r')
    fig = plt.gcf()
    ax = fig.gca() # gca() signifie Obtenir l'axe actuel
    ax.set_aspect(ratio) # je choisi le ratio DX/DY pour les echelles des
    ax.add_artist(Ellipse((x, y), rayon*ratio, rayon,color='yellow',alpha=0.2))
    plt.legend()
    plt.show()
joueur(9, 20)
filtre = tableau_reduit['poste'] == 'G'
df_G= tableau_reduit[filtre]
filtre = tableau_reduit['poste'] == 'C'
df_C = tableau_reduit[filtre]
filtre = tableau_reduit['poste'] == 'F'
df_F = tableau_reduit[filtre]
ensemble = pd.concat([df_G,df_C,df_F])
print(ensemble.head())
def distance(num,ratio):
    x1 = tableau_reduit.loc[num]['taille']
    y1 = tableau_reduit.loc[num]['poids']
    ensemble['dist'] = ensemble.apply(lambda row: (((row["taille"] -x1)/ratio)**2 + (row["poids"] - y1)**2)**0.5, axis=1)
print(distance(9, 0.005))
print(ensemble.head())
df2=ensemble.sort_values(by='dist')
print(df2.head())

from matplotlib.patches import Ellipse, Circle


def knn(k):
    result = {'G': 0, 'F': 0, 'C': 0}

    for i in range(k):
        position = df2.iloc[i]['poste']
        result[position] += 1

    return result

# Example usage to find the 8 and 10 nearest neighbors for player 9
k_8 = 8
k_10 = 10

# Assuming you already have the distance function defined

# Calculate distances for player 9
distance(9, 0.005)

# Sort the ensemble DataFrame based on distances
df2 = ensemble.sort_values(by='dist')

# Find the k-nearest neighbors
neighbors_8 = knn(k_8)
neighbors_10 = knn(k_10)

print(f"8 Nearest Neighbors: {neighbors_8}")
print(f"10 Nearest Neighbors: {neighbors_10}")


