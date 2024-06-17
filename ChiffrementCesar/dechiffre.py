def decale_lettre(lettre, decalage):
    # Gère le chiffrement/déchiffrement des lettres en majuscule.
    if 'A' <= lettre <= 'Z':
        return chr((ord(lettre) - ord('A') + decalage) % 26 + ord('A'))
    # Gère le chiffrement/déchiffrement des lettres en minuscule.
    elif 'a' <= lettre <= 'z':
        return chr((ord(lettre) - ord('a') + decalage) % 26 + ord('a'))
    else:
        return lettre

def dechiffrer_cesar(texte_chiffre, decalage):
    texte_dechiffre = ''.join(decale_lettre(lettre, decalage) for lettre in texte_chiffre)
    return texte_dechiffre

def brute_force_cesar(texte_chiffre):
    possibles_dechiffres = []
    for cle in range(26):
        texte_dechiffre = dechiffrer_cesar(texte_chiffre, -cle)
        possibles_dechiffres.append((cle, texte_dechiffre))
    return possibles_dechiffres

# Exemple de texte chiffré
texte_chiffre = "D.O.Y.O.B"

# Essai de toutes les clés pour trouver le texte original
resultats = brute_force_cesar(texte_chiffre)

for cle, texte in resultats:
    print(f"Clé {cle}: {texte}")
