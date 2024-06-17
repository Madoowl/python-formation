import os

# Spécifiez le chemin du dossier
folder_path = './'  # Remplacez par le chemin de votre dossier

# Lister les fichiers dans le dossier
files = os.listdir(folder_path)

# Filtrer pour obtenir uniquement les fichiers (et non les sous-dossiers)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

print("Fichiers dans le dossier :", files)
