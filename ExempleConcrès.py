import pandas as pd
import streamlit as st
from scipy.cluster import hierarchy
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Mall_Customers.csv')

# # # Prétraitement des données # # #

print(data.head())  # afficher les en-tete de la data
print(data.isnull().sum)  # vérifier s'il y a des valeur manquantes


# # # Choix de la mesure de similarité et calcul de matrice de distance # # #

colonnes_a_utiliser = ['Revenu Annuel (k$)', 'Depense quotidienne (1-100)']  # Sélectionner les colonnes à utiliser pour le calcul de la distance

donnees = data[colonnes_a_utiliser].values  # Extraire les données à partir des colonnes sélectionnées


matrice_distance = euclidean_distances(donnees)  # Calculer la matrice de distance euclidienne

df_distance = pd.DataFrame(matrice_distance, index=data.index, columns=data.index)  # Créer un DataFrame à partir de la matrice de distance
st.write('Matrice de distance entre chaque pair de clusters')
st.write(df_distance)  # Afficher la  matrice de distance

# # # Choix de la mesure de fusion pour combiner les clusters selon leur similarité # # #

clustering = AgglomerativeClustering(linkage='complete')  # Créer une instance de AgglomerativeClustering en utilisant la méthode de liaison complète
clusters = clustering.fit_predict(df_distance)  # Appliquer le clustering sur vos données
st.write('Affichage des sous catégories de clusters')
st.write(clusters)  # Affichage des sous gatégories de clusters dans un tableau

# # # Appliquez l'algorithme de clustering hiérarchique pour afficher des clusters # # #

# Convertir les clusters en DataFrame
df_clusters = pd.DataFrame({'Revenu Annuel (k$)': data['Revenu Annuel (k$)'],
                            'Depense quotidienne (1-100)': data['Depense quotidienne (1-100)'],
                            'Cluster': clusters})
st.write('Affichage des clusters')
sns.set(style="whitegrid")  # Définir le style des graphiques

# Créer un scatter plot pour visualiser les clusters
plt.figure(figsize=(10, 6))  # fonction permettant de créer une nouvelle figure avec ne taille de 10 pouces de largeur et 6 pouces de hauteur
# crée un graphique de dispersion (scatter plot) avec Seaborn
sns.scatterplot(x='Revenu Annuel (k$)', y='Depense quotidienne (1-100)', hue='Cluster', data=df_clusters, palette='tab10',
                legend='full')
plt.title('Visualisation des clusters')  # fonction pour attribuer un titre au graphique
plt.xlabel('Revenu Annuel (k$)')  # fonction pour déterminer la donnée qui sera l'axe x
plt.ylabel('Depense quotidienne (1-100)')  # fonction pour déterminer la donnée qui sera l'axe y
plt.savefig('scatter_plot_clusters.png')  # fonction pour enregistrer le graphique dans un fichier image
st.image('scatter_plot_clusters.png')  # fonction pour Afficher le graphique avec Streamlit

# # # Créer le dendrogramme , l'afficher et analysé # # #

st.write('Dendogramme')
plt.figure(figsize=(12, 6))  # fonction permettant de créer une nouvelle figure avec ne taille de 12 pouces de largeur et 6 pouces de hauteur
dendrogram = hierarchy.dendrogram(hierarchy.linkage(matrice_distance, method='ward'), labels=data.index)
plt.title('Dendrogramme')   # fonction pour attribuer un titre au dendogramme
plt.xlabel('Échantillons')  # fonction pour déterminer la donnée qui sera l'axe x
plt.ylabel('Distance')  # fonction pour déterminer la donnée qui sera de l'axe y
plt.xticks(rotation=100)   # fontion pour faire pivoter les étiquettes sur l'axe des x de 100
plt.tight_layout()   # fonction permettant d'éviter que les étiquettes ou les titres ne se chevauchent.
plt.savefig('dendogramme_clusters.png')  # Enregistrer le graphique dans un fichier image
st.image('dendogramme_clusters.png')  # Afficher le graphique avec Streamlit
# Analyse