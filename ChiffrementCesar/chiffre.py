def chiffrement_cesar(mot, cle):
    mot_chiffre = ""
    for lettre in mot:
        if 'A' <= lettre <= 'Z':  # Si la lettre est une majuscule
            mot_chiffre += chr((ord(lettre) - ord('A') + cle) % 26 + ord('A'))
        elif 'a' <= lettre <= 'z':  # Si la lettre est une minuscule
            mot_chiffre += chr((ord(lettre) - ord('a') + cle) % 26 + ord('a'))
        else:
            mot_chiffre += lettre  # Si ce n'est pas une lettre, on ne change pas le caractère
    return mot_chiffre

def main():
    mot = input("Entrez le mot à chiffrer: ")
    cle = int(input("Entrez la clé de chiffrement (un nombre entre 1 et 25): "))
    while not 1 <= cle <= 25:
        print("La clé doit être un nombre entre 1 et 25.")
        cle = int(input("Entrez la clé de chiffrement (un nombre entre 1 et 25): "))
    
    mot_chiffre = chiffrement_cesar(mot, cle)
    print(f"Le mot chiffré est: {mot_chiffre}")

if __name__ == "__main__":
    main()
