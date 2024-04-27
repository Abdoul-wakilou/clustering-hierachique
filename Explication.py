import streamlit as st

st.title("Explication de l’algorithme du clustering hiérachique:")
st.write(
    "L'algorithme de clustering hiérarchique commence par considérer chaque point de données comme un cluster individuel. Ensuite, "
    "il calcule itérativement la similarité entre chaque paire de clusters et "
    "fusionne les clusters les plus similaires pour former des clusters plus grands. "
    "Ce processus est répété jusqu'à ce qu'un seul cluster contenant toutes les données soit obtenu. "
    "Il existe deux approches principales dans l'algorithme de clustering hiérarchique :")
st.write(
    "**- Agrégatif (ou ascendante)**: Dans cette approche, chaque point de données est initialement considéré comme un cluster séparé, puis les clusters sont fusionnés progressivement en fonction de leur similarité. Cette méthode produit un dendrogramme, une structure arborescente représentant la hiérarchie des clusters.")
st.write(
    "**- Divisif (ou descendante)**: Contrairement à l('approche agrégative, cette méthode commence avec un seul cluster contenant tous les points de données et divise récursivement ce cluster en sous-clusters plus petits ' "
    "'jusqu')à ce que chaque point de données soit dans son propre cluster. ")
st.write(
    "Pour effectuer du clustering hiérarchique sur votre ensemble de données, vous pouvez suivre ces étapes générales : ")

st.write(
    "**Prétraitement des données** : Vérifiez s'il y a des valeurs manquantes dans votre ensemble de données et décidez comment les gérer (imputation, suppression, etc.).Si nécessaire, normalisez vos données pour que les variables soient sur la même échelle, car le clustering hiérarchique est sensible aux écarts d'échelle entre les variables.")
st.write("**Choix de la mesure de similarité/distinction** : "
         "Choisissez une mesure de similarité/distinction appropriée pour calculer la distance entre les observations. Cela dépendra de la nature de vos données. Par exemple, la distance euclidienne est souvent utilisée pour les variables numériques, tandis que des mesures telles que la distance de Jaccard peuvent être utilisées pour les variables catégorielles.")
st.write("**Construction de la matrice de distance** : "
         "Utilisez la mesure de similarité/distinction choisie pour calculer une matrice de distance entre les observations dans votre ensemble de données.")
st.write("**Choix de la méthode de fusion** : "
         "Choisissez une méthode de fusion pour combiner les clusters à chaque étape de l'algorithme. Les méthodes couramment utilisées incluent la liaison simple, la liaison complète, la liaison moyenne, etc.")
st.write(
    "**Clustering hiérarchique** : Appliquez l'algorithme de clustering hiérarchique en utilisant la matrice de distance et la méthode de fusion choisies. ")
st.write(
    "**Interprétation des résultats** : Analysez le dendrogramme résultant pour déterminer le nombre de clusters à choisir en fonction de la structure de l'arbre et de vos besoins d'application.")
