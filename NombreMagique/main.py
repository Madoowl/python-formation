import random

def jeu_devinette():
    # Générer un nombre aléatoire entre 1 et 45
    nombre_a_deviner = random.randint(1, 45)
    devine = None
    tentatives = 0

    print("Bienvenue au jeu de devinette !")
    print("Je pense à un nombre entre 1 et 45.")
    print("Pouvez-vous deviner lequel ?")

    # Boucle jusqu'à ce que l'utilisateur devine correctement
    while devine != nombre_a_deviner:
        try:
            devine = int(input("Entrez votre devinette : "))
            tentatives += 1
            
            if devine < 1 or devine > 45:
                print("S'il vous plaît, entrez un nombre entre 1 et 45.")
            elif devine < nombre_a_deviner:
                print("C'est plus grand ! Essayez encore.")
            elif devine > nombre_a_deviner:
                print("C'est plus petit ! Essayez encore.")
            else:
                print(f"Bravo ! Vous avez deviné le nombre {nombre_a_deviner} en {tentatives} tentatives.")
        except ValueError:
            print("Entrée invalide. S'il vous plaît, entrez un nombre entier.")

# Appel de la fonction pour démarrer le jeu
jeu_devinette()
