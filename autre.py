import fig
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
print(data.isnull().sum) # vérifier s'il y a des valeur manquantes

# mettre les donnees au meme echelle en sélectionner les colonnes numériques pour la normalisation
# colonnesnumeriques = ['Annual Income (k$)', 'Spending Score (1-100)']

# Normaliser les données numériques
# scaler = StandardScaler()
# data[colonnesnumeriques] = scaler.fit_transform(data[colonnesnumeriques])

# # # Choix de la mesure de similarité et calcul de matrice de distance # # #
# Sélectionner les colonnes à utiliser pour le calcul de la distance
colonnes_a_utiliser = ['Annual Income (k$)', 'Spending Score (1-100)']

# Extraire les données à partir des colonnes sélectionnées
donnees = data[colonnes_a_utiliser].values

# Calculer la matrice de distance euclidienne
matrice_distance = euclidean_distances(donnees)

# Créer un DataFrame à partir de la matrice de distance
df_distance = pd.DataFrame(matrice_distance, index=data.index, columns=data.index)
st.write('Matrice de distance entre chaque pair de clusters')
st.write(df_distance)

# # # Choix de la mesure de similarité et calcul de matrice de distance # # #


# Créer une instance de AgglomerativeClustering avec la méthode de liaison complète
clustering = AgglomerativeClustering(linkage='complete')

# Appliquer le clustering sur vos données
clusters = clustering.fit_predict(df_distance)
st.write('Affichage des sous gatégories de clusters')
st.write(clusters)

# # # Affichage des clusters # # #


# Définir le style des graphiques
# Convertir les clusters en DataFrame
df_clusters = pd.DataFrame({'Annual Income (k$)': data['Annual Income (k$)'],
                            'Spending Score (1-100)': data['Spending Score (1-100)'],
                            'Cluster': clusters})

# Définir le style des graphiques
st.write('Affichage de chaque point de données')
sns.set(style="whitegrid")

# Créer un scatter plot pour visualiser les clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=df_clusters, palette='tab10',
                legend='full')
plt.title('Visualisation des clusters')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')

# Enregistrer le graphique dans un fichier image
plt.savefig('scatter_plot_clusters.png')

# Afficher le graphique avec Streamlit
st.image('scatter_plot_clusters.png')

# Créer un dendrogramme
st.write('Dendogramme')
plt.figure(figsize=(12, 6))
dendrogram = hierarchy.dendrogram(hierarchy.linkage(matrice_distance, method='ward'), labels=data.index)
plt.title('Dendrogramme')
plt.xlabel('Échantillons')
plt.ylabel('Distance')
plt.xticks(rotation=90)
plt.tight_layout()

# Enregistrer le graphique dans un fichier image
plt.savefig('dendogramme_clusters.png')

# Afficher le graphique avec Streamlit
st.image('dendogramme_clusters.png')
