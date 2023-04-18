from fonctions import *

a = Sommet(5, 'a')
b = Sommet(3, 'b')
c = Sommet(7, 'c')

arbre_a = ArbreB(a)
#arbre_a.inserer_arbre(ArbreB(b))
arbre_a = arbre_a + ArbreB(b)
#arbre_a.inserer_arbre(ArbreB(c))
arbre_a += ArbreB(c)

print(arbre_a.get_gauche().racine.valeur)
print(arbre_a.get_gauche().racine.lettre)
print()
print(arbre_a.get_droit().racine.valeur)
print(arbre_a.get_droit().racine.lettre)
print()
arbre_a.supprimer_arbre(7)
#arbre_a = arbre_a - 7
print(arbre_a.get_droit().racine.valeur)
print(arbre_a.get_droit().racine.lettre)

#arbre_a = arbre_a + ArbreB(Sommet(8, 'd'))
#arbre_a.inserer_arbre(Sommet(8, 'd'))

#print(arbre_a.get_droit().get_gauche())
#valeur = 4

#if valeur in arbre_a:
    #print(f"{valeur} est dans l'arbre")
#else:
    #print(f"{valeur} n'est pas dans l'arbre")





#d = Sommet(4, 'd')
#e = Sommet(2, 'e')
#f = Sommet(8, 'f')
#arbre_b = ArbreB(d)
#arbre_b.inserer_arbre(ArbreB(e))
#arbre_b.inserer_arbre(ArbreB(f))

#arbre_a.fusion(arbre_b)

#decomposition = arbre_a.decomposition()
#for arbre in decomposition:
#    print(arbre.valeur)

#print(arbre_a.get_racine().valeur)
#print(arbre_a.get_gauche().get_racine().valeur)
#print(arbre_a.get_droit().get_racine().valeur)
#print(arbre_a.get_gauche().get_gauche().get_racine().valeur)
#print(arbre_a.get_gauche().get_droit().get_racine().valeur)
#print(arbre_a.get_droit().get_droit().get_racine().valeur)

#arbre_a.inserer_arbre(ArbreB(Sommet(4, 'd')))

#arbre_a.supprimer_arbre(7)

#print(arbre_a.get_racine().valeur)
#print(arbre_a.get_gauche().get_droit().get_racine().lettre)
#print(arbre_a.get_droit().get_racine().lettre))

#arbre_a.modifier_etiquette_arbre(5, 7)
#print(arbre_a.get_racine().valeur)
#print(arbre_a.rechercher_element(4).get_racine().lettre)
