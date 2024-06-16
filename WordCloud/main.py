import json
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud

# Téléchargement des ressources nécessaires de nltk
nltk.download('stopwords')

# Liste des insultes à filtrer
insultes = ["merde", "chips", "insulte3"]  # Remplacer par de vraies insultes
data = json.load(open('data.json'))
# Texte d'exemple
texte = """
Votre texte ici. Ajoutez du texte avec des mots variés pour tester le nuage de mots.
"""

# Fonction pour filtrer les insultes
def filtrer_insultes(mots, insulte):
    return [mot for mot in mots if mot.lower() not in data]

# Traitement du texte
mots = data
mots_filtres = filtrer_insultes(mots, insultes)

# Génération du nuage de mots
nuage_de_mots = WordCloud(
    width=800, height=400,
    background_color='white',
    stopwords=set(stopwords.words('french'))  # Exclure les mots vides courants
).generate(" ".join(mots_filtres))

# Affichage du nuage de mots
plt.figure(figsize=(10, 5))
plt.imshow(nuage_de_mots, interpolation='bilinear')
plt.axis('off')
plt.show()