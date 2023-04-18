# PARTIE 1

# Question 1.1 et 1.2

import tkinter as tk

class Sommet(object):
    def __init__(self, valeur: float, lettre: int=None):
        """
        Initialise un objet Sommet avec une valeur et une lettre optionnelle.
        :param valeur: La valeur du sommet.
        :param lettre: La lettre associée au sommet (optionnelle).
        """
        self.valeur = valeur
        self.lettre = lettre


class ArbreB(object):
    def __init__(self, racine: Sommet, gauche=None, droite=None):
        """
        Initialise un objet ArbreB avec une racine et des sous-arbres gauche et droit optionnels.
        :param racine: L'objet Sommet qui est la racine de l'arbre.
        :param gauche: L'objet ArbreB qui est le sous-arbre gauche de l'arbre (optionnel).
        :param droite: L'objet ArbreB qui est le sous-arbre droit de l'arbre (optionnel).
        """
        self.racine = racine
        self.gauche = gauche
        self.droite = droite

    def get_racine(self):
        """
        Retourne un objet Sommet qui est la racine de l'arbre.
        :return: L'objet Sommet qui est la racine de l'arbre.
        """
        return self.racine

    def get_gauche(self):
        """
        Retourne un objet ArbreB qui est le sous-arbre gauche de l'arbre.
        :return: L'objet ArbreB qui est le sous-arbre gauche de l'arbre.
        """
        return self.gauche

    def get_droit(self):
        """
        Retourne un objet ArbreB qui est le sous-arbre droit de l'arbre.
        :return: L'objet ArbreB qui est le sous-arbre droit de l'arbre.
        """
        return self.droite
    
    def inserer_arbre(self, arbre): # inserer_sommet()
        """
        Insère un objet ArbreB dans l'arbre binaire de recherche.
        :param arbre: L'objet ArbreB à insérer dans l'arbre binaire de recherche.
        """
        if arbre.racine.valeur < self.racine.valeur:
            if self.gauche is None:
                self.gauche = arbre
            else:
                self.gauche.inserer_arbre(arbre)
        else:
            if self.droite is None:
                self.droite = arbre
            else:
                self.droite.inserer_arbre(arbre)

    def __add__(self, arbre):
        """
        Surcharge de l'opérateur + pour insérer un objet ArbreB dans l'arbre binaire de recherche.
        :param arbre: L'objet ArbreB à insérer dans l'arbre binaire de recherche.
        :return: L'objet ArbreB qui est l'arbre binaire de recherche après l'insertion.
        """
        if arbre.get_gauche() is None and arbre.get_droit() is None:
            self.inserer_arbre(arbre)
            return self
        else:
            self.fusion(arbre)
            return self
    
    def __iadd__(self, arbre):
        """
        Surcharge de l'opérateur += pour insérer un objet ArbreB dans l'arbre binaire de recherche.
        :param arbre: L'objet ArbreB à insérer dans l'arbre binaire de recherche.
        :return: L'objet ArbreB qui est l'arbre binaire de recherche après l'insertion.
        """
        if arbre.get_gauche() is None and arbre.get_droit() is None:
            self.inserer_arbre(arbre)
            return self
        else:
            self.fusion(arbre)
            return self

    def supprimer_arbre(self, valeur): # supprimer sommet
        """
        Supprime un objet ArbreB avec une valeur donnée de l'arbre binaire de recherche.
        :param valeur: La valeur de l'objet ArbreB à supprimer de l'arbre binaire de recherche.
        :return: L'objet ArbreB qui est l'arbre binaire de recherche après la suppression.
        """
        if self.racine.valeur == valeur:
            if self.gauche is None and self.droite is None:
                return None
            elif self.gauche is None:
                return self.droite
            elif self.droite is None:
                return self.gauche
            else:
                successeur = self.droite
                while successeur.gauche is not None:
                    successeur = successeur.gauche
                self.racine = successeur.racine
                self.droite = self.droite.supprimer_arbre(successeur.racine.valeur)
                return self
        elif valeur < self.racine.valeur and self.gauche is not None:
            self.gauche = self.gauche.supprimer_arbre(valeur)
            return self
        elif valeur > self.racine.valeur and self.droite is not None:
            self.droite = self.droite.supprimer_arbre(valeur)
            return self
        else:
            return self

    def __sub__(self, valeur):
        """
        Surcharge de l'opérateur - pour supprimer un objet ArbreB avec une valeur donnée de l'arbre binaire de recherche.
        :param valeur: La valeur de l'objet ArbreB à supprimer de l'arbre binaire de recherche.
        :return: L'objet ArbreB qui est l'arbre binaire de recherche après la suppression.
        """
        self.supprimer_arbre(valeur)
        return self
    
    def __isub__(self, valeur):
        """
        Surcharge de l'opérateur -= pour supprimer un objet ArbreB avec une valeur donnée de l'arbre binaire de recherche.
        :param valeur: La valeur de l'objet ArbreB à supprimer de l'arbre binaire de recherche.
        :return: L'objet ArbreB qui est l'arbre binaire de recherche après la suppression.
        """
        self.supprimer_arbre(valeur)
        return self

    def modifier_etiquette_lettre_arbre(self, lettre, nouvelle_lettre):
        """
        Modifie l'étiquette d'un objet ArbreB avec une lettre donnée dans l'arbre binaire de recherche.
        :param lettre: La lettre de l'objet ArbreB dont l'étiquette doit être modifiée.
        :param nouvelle_lettre: La nouvelle lettre à attribuer à l'étiquette de l'objet ArbreB.
        """
        if self.racine.lettre == lettre:
            self.racine.lettre = nouvelle_lettre
        elif self.gauche is not None:
            self.gauche.modifier_etiquette_lettre_arbre(lettre, nouvelle_lettre)
        elif self.droite is not None:
            self.droite.modifier_etiquette_lettre_arbre(lettre, nouvelle_lettre)
        
    def modifier_etiquette_valeur_arbre(self, lettre, nouvelle_valeur):
        """
        Modifie l'étiquette d'un objet ArbreB avec une valeur donnée dans l'arbre binaire de recherche.
        :param lettre: La lettre de l'objet ArbreB dont l'étiquette doit être modifiée.
        :param nouvelle_valeur: La nouvelle valeur à attribuer à l'étiquette de l'objet ArbreB.
        """
        if self.racine.lettre == lettre:
            self.racine.valeur = nouvelle_valeur
        elif self.gauche is not None:
            self.gauche.modifier_etiquette_valeur_arbre(lettre, nouvelle_valeur)
        elif self.droite is not None:
            self.droite.modifier_etiquette_valeur_arbre(lettre, nouvelle_valeur)

    def rechercher_element(self, valeur):
        """
        Recherche un objet ArbreB avec une valeur donnée dans l'arbre binaire de recherche.
        :param valeur: La valeur de l'objet ArbreB à rechercher dans l'arbre binaire de recherche.
        :return: L'objet ArbreB trouvé ou None si aucun objet ArbreB avec la valeur donnée n'est trouvé.
        """
        if self.racine.valeur == valeur:
            return self
        elif self.gauche and valeur < self.racine.valeur:
            return self.gauche.rechercher_element(valeur)
        elif self.droite and valeur > self.racine.valeur:
            return self.droite.rechercher_element(valeur)
        else:
            return None

    def fusion(self, autre_arbre):
        """
        Fusionne un autre arbre binaire de recherche avec cet arbre binaire de recherche.
        :param autre_arbre: L'arbre binaire de recherche à fusionner avec cet arbre binaire de recherche.
        """
        if autre_arbre is not None:
            if self.racine is None:
                self.racine = autre_arbre.racine
                self.gauche = autre_arbre.gauche
                self.droite = autre_arbre.droite
            elif autre_arbre.racine.valeur < self.racine.valeur:
                if self.gauche is None:
                    self.gauche = ArbreB(autre_arbre.racine, autre_arbre.gauche, autre_arbre.droite)
                else:
                    self.gauche.fusion(autre_arbre)
            else:
                if self.droite is None:
                    self.droite = ArbreB(autre_arbre.racine, autre_arbre.gauche, autre_arbre.droite)
                else:
                    self.droite.fusion(autre_arbre)

    def decomposition(self):
        """
        Décompose cet arbre binaire de recherche en une liste d'éléments.
        :return: Une liste d'objets Sommet représentant les éléments de l'arbre binaire de recherche.
        """
        elements = []
        if self.gauche is not None:
            elements.extend(self.gauche.decomposition())
        elements.append(self.racine)
        if self.droite is not None:
            elements.extend(self.droite.decomposition())
        return elements

    def __str__(self):
        """
        Surcharge de la méthode str pour afficher l'arbre binaire de recherche.
        :return: Une chaîne de caractères représentant l'arbre binaire de recherche.
        """
        return str([(str(arbre.lettre),str(arbre.valeur)) for arbre in self.decomposition()])

# Question 1.3

def test_arbre_binaire():
    """
    Fonction de test de la classe ArbreB.
    """
    # Définition des sommets de base
    sommet_a = Sommet(1, "A")
    sommet_b = Sommet(2, "B")
    sommet_c = Sommet(3, "C")
    # Création du premier arbre
    arbre1 = ArbreB(sommet_a)
    arbre1 += ArbreB(sommet_b)
    arbre1 += ArbreB(sommet_c)
    # Affichage du premier arbre
    print("Arbre 1 :")
    print(arbre1)
    # Création du deuxième arbre
    arbre2 = ArbreB(Sommet(4, "D"))
    arbre2 += ArbreB(Sommet(5, "E"))
    arbre2 += ArbreB(Sommet(6, "F"))
    # Fusion avec le premier arbre
    arbre1 += arbre2
    # Affichage du premier arbre après fusion
    print("Arbre 1 après fusion :")
    print(arbre1)
    # Suppression d'un élément
    arbre1 -= 3
    # Affichage du premier arbre après fusion et suppression
    print("Arbre 1 après fusion et suppression :")
    print(arbre1)
    # Modification de l'étiquette lettre d'un élément
    arbre1.modifier_etiquette_lettre_arbre('D', 'Z')
    # Affichage du premier arbre après fusion, suppression et modification
    print("Arbre 1 après fusion, suppression et modification :")
    print(arbre1)
    # Modification de l'étiquette valeur d'un élément
    arbre1.modifier_etiquette_valeur_arbre('Z', 7)
    # Affichage du premier arbre après fusion, suppression, modification et modification
    print("Arbre 1 après fusion, suppression, modification et modification :")
    print(arbre1)
    # Recherche d'un élément
    print("Recherche de l'élément 3 :")
    print(arbre1.rechercher_element(2))
    # Recherche d'un élément non présent
    print("Recherche de l'élément 10 :")
    print(arbre1.rechercher_element(10))

# Question 1.4 - Développer une interface graphique pour la représentation de l'arbre binaire de recherche.

class ArbreBinaire(tk.Canvas):
    def __init__(self, master, arbre, *args, **kwargs):
        """
        Constructeur de la classe ArbreBinaire.
        :param master: La fenêtre parente.
        :param arbre: L'arbre binaire de recherche à afficher.
        :param args: Arguments supplémentaires.
        :param kwargs: Arguments nommés supplémentaires.
        """
        tk.Canvas.__init__(self, master, *args, **kwargs)
        self.arbre = arbre
        self.width = 800
        self.height = 600
        self.diametre_cercle = 50
        self.espacement_horiz = 50
        self.espacement_vert = 100
        self.positions = {}

    def afficher(self):
        """
        Affiche l'arbre binaire de recherche.
        """
        self.delete(tk.ALL)
        self.positions.clear()
        self._afficher_sous_arbre(self.arbre, self.width / 2, 0, self.width / 4)

    def _afficher_sous_arbre(self, arbre, x, y, h):
        """
        Affiche un sous-arbre de l'arbre binaire de recherche.
        :param arbre: Le sous-arbre à afficher.
        :param x: La position horizontale du sous-arbre.
        :param y: La position verticale du sous-arbre.
        :param h: La hauteur du sous-arbre.
        :return: Le sous-arbre à afficher.
        """
        if arbre is not None:
            gauche = self._afficher_sous_arbre(arbre.gauche, x - h, y + self.espacement_vert, h / 2)
            droite = self._afficher_sous_arbre(arbre.droite, x + h, y + self.espacement_vert, h / 2)
            cercle = self.create_oval(x - self.diametre_cercle / 2, y, x + self.diametre_cercle / 2,
                                      y + self.diametre_cercle, fill="white", width=2)
            texte = self.create_text(x, y + self.diametre_cercle / 2, text=str(arbre.racine.valeur))
            self.positions[arbre] = (x, y, cercle, texte)
            if gauche is not None:
                self.create_line(x, y + self.diametre_cercle / 2, gauche[0], gauche[1] + self.diametre_cercle / 2, width=2)
            if droite is not None:
                self.create_line(x, y + self.diametre_cercle / 2, droite[0], droite[1] + self.diametre_cercle / 2, width=2)
            return x, y
        else:
            return None
        

def test_interface_graphique():
    """
    Fonction de test de l'interface graphique.
    """
    # Création de la fenêtre
    fenetre = tk.Tk()
    fenetre.title("Arbre binaire de recherche")
    # Création de l'arbre binaire de recherche
    arbre = ArbreB(Sommet(8, "A"))
    arbre += ArbreB(Sommet(5, "B"))
    arbre += ArbreB(Sommet(10, "C"))
    arbre += ArbreB(Sommet(2, "D"))
    arbre += ArbreB(Sommet(3, "E"))
    arbre += ArbreB(Sommet(9, "F"))
    # Création de l'interface graphique
    interface_graphique = ArbreBinaire(fenetre, arbre, width=800, height=600)
    interface_graphique.pack()
    interface_graphique.afficher()
    # Affichage de la fenêtre
    fenetre.mainloop()

test_interface_graphique()