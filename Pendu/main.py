import random

def choisir_mot():
    mots = ["python", "developpement", "ordinateur", "programme", "intelligence", "artificielle", "pendu", "algorithmique"]
    return random.choice(mots)

def afficher_mot(mot, lettres_trouvees):
    affichage = ''.join([lettre if lettre in lettres_trouvees else '_' for lettre in mot])
    return affichage

def jouer_au_pendu():
    mot_a_trouver = choisir_mot()
    lettres_trouvees = set()
    lettres_essayees = set()
    essais_restants = 6

    print("Bienvenue au jeu de Pendu!")
    print("Vous avez 6 essais pour deviner le mot.")

    while essais_restants > 0:
        print("\nMot à deviner: ", afficher_mot(mot_a_trouver, lettres_trouvees))
        print(f"Essais restants: {essais_restants}")
        print("Lettres essayées: ", ' '.join(sorted(lettres_essayees)))

        lettre = input("Proposez une lettre: ").lower()

        if lettre in lettres_essayees:
            print("Vous avez déjà essayé cette lettre.")
            continue

        lettres_essayees.add(lettre)

        if lettre in mot_a_trouver:
            lettres_trouvees.add(lettre)
            print("Bonne réponse!")

            if all(lettre in lettres_trouvees for lettre in mot_a_trouver):
                print("\nFélicitations! Vous avez trouvé le mot:", mot_a_trouver)
                break
        else:
            essais_restants -= 1
            print("Mauvaise réponse!")

    if essais_restants == 0:
        print("\nDésolé, vous avez perdu. Le mot était:", mot_a_trouver)

if __name__ == "__main__":
    jouer_au_pendu()
