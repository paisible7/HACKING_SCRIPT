import itertools
import string

nomFichier = "dictionnaire.txt"

chars = string.ascii_letters + string.digits

def generate_combinaisons_with_prefixe(prefixe, taille):

    with open(nomFichier, "w") as file:
        caractere = taille - len(prefixe)
        
        if caractere > 0:
            for combinaison in itertools.product(chars, repeat=caractere):
                file.write(prefixe + ''.join(combinaison) + "\n")
        else:
            file.write(prefixe + "\n")

prefixe = "a"

taille = 8

generate_combinaisons_with_prefixe(prefixe, taille)
