# PARTIE 2

from main import *

# Question 1

def occurence(texte):
    occurence = dict()
    texte_list = list(texte.lower())
    while " " in texte_list:
        texte_list.remove(" ")
    for lettre in set(texte_list):
        occurence[lettre] = round((texte_list.count(lettre) / len(texte_list)), 2)
        #occurence[lettre] = "{0:.2%}".format(round((texte_list.count(lettre) / len(texte_list)), 4))
    return occurence

# Question 2

def construire_arbreB_Huffman(texte):
    # Étape 1 : Créer liste de sommets/arbres pour chaque lettre du texte
    dict_occurence = occurence(texte)
    liste_sommets = []
    for lettre, occ in dict_occurence.items():
        liste_sommets.append(ArbreB(Sommet(occ, lettre)))
    # Étape 2 : Construire l'arbre
    # 
    sommet_1 = liste_sommets[0]
    sommet_2 = liste_sommets[1]
    for i in range(2, len(liste_sommets)):
        if sommet_1.get_racine().valeur > liste_sommets[i].get_racine().valeur:
            sommet_1 = liste_sommets[i]
    liste_sommets.remove(sommet_1)
    for i in range(2, len(liste_sommets)):
        if sommet_2.get_racine().valeur > liste_sommets[i].get_racine().valeur:
            sommet_2 = liste_sommets[i]
    liste_sommets.remove(sommet_2)
    sommet_3 = ArbreB(Sommet(valeur=(sommet_1.get_racine().valeur + sommet_2.get_racine().valeur)),
                      sommet_1, sommet_2)
    liste_sommets.append(sommet_3)
    return liste_sommets, sommet_1, sommet_2, sommet_3
    
def construire_arbreB_Huffman(texte):
    # Étape 1 : Créer liste de sommets/arbres pour chaque lettre du texte
    dict_occurence = occurence(texte)
    liste_sommets = []
    for lettre, occ in dict_occurence.items():
        liste_sommets.append(ArbreB(Sommet(occ, lettre)))

    # Étape 2 : Construire l'arbre
    while len(liste_sommets) > 1:
        sommet_1 = liste_sommets[0]
        sommet_2 = liste_sommets[1]
        for i in range(2, len(liste_sommets)):
            if sommet_1.get_racine().valeur > liste_sommets[i].get_racine().valeur:
                sommet_1 = liste_sommets[i]
        liste_sommets.remove(sommet_1)
        for i in range(2, len(liste_sommets)):
            if sommet_2.get_racine().valeur > liste_sommets[i].get_racine().valeur:
                sommet_2 = liste_sommets[i]
        liste_sommets.remove(sommet_2)
        sommet_3 = ArbreB(Sommet(valeur=(sommet_1.get_racine().valeur + sommet_2.get_racine().valeur)),
                          sommet_1, sommet_2)
        liste_sommets.append(sommet_3)

    # Étape 3 : Retourner l'arbre de Huffman
    return liste_sommets[0]