"""from fonctions import *

sommets = {lettre for lettre in test}

sommets = [Sommet(lettre) for lettre in sommets]

#for lettre in sommets:
#    print(lettre.lettre, lettre.occurence)

arbre_etape_1 = [ArbreB(sommet) for sommet in sommets]

def fusion(arbre_1, arbre_2):
    racine = arbre_1.racine + arbre_2.racine
    fils_gauche = arbre_1
    fils_droit = arbre_2
    return ArbreB(racine, fils_gauche, fils_droit)
"""

my_iter = iter([1, 2, 3])
print(next(my_iter)) # 1
print(next(my_iter)) # 2
print(next(my_iter)) # 3
print(next(my_iter, "abc")) # Erreur StopIteration