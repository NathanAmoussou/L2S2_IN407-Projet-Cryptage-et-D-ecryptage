import tkinter as tk
import math

# PARTIE 1

# Question 1.1 et 1.2

class Sommet(object):
    def __init__(self, valeur: float, lettre: str=None):
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
    def __init__(self, master, arbre, t=None, *args, **kwargs):
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
        self.t = t

    def afficher(self):
        """
        Affiche l'arbre binaire de recherche.
        """
        self.delete(tk.ALL) # Efface le contenu de la zone de dessin
        self.positions.clear() # Vide le dictionnaire des positions
        self._afficher_sous_arbre(self.arbre, self.width / 2, 0, self.width / 4) # Affiche le sous-arbre
        x1, y1, x2, y2 = self.bbox(tk.ALL) # Récupère les coordonnées de la zone de dessin
        self.configure(width=x2-x1+100, height=y2-y1+200) # Redimensionne la zone de dessin
        self.xview_moveto((x1-50)/(x2-x1+100)) # Centre la zone de dessin
        self.yview_moveto(0) # Place la zone de dessin en haut
        chemins = trouver_chemins_feuilles(self.arbre, []) # Récupère les chemins des feuilles
        texte = "Codage de Huffman : " + ''.join([str(chiffre) for lettre in self.t for chiffre in chemins[lettre]]) # Crée le texte à afficher
        self.create_text(self.width / 2, y2 + 50, text=texte) # Affiche le texte

    def _afficher_sous_arbre(self, arbre, x, y, h):
        """
        Affiche un sous-arbre de l'arbre binaire de recherche.
        :param arbre: Le sous-arbre à afficher.
        :param x: La position horizontale du sous-arbre.
        :param y: La position verticale du sous-arbre.
        :param h: La hauteur du sous-arbre.
        :return: Le sous-arbre à afficher.
        """
        if arbre is not None: # Si l'arbre n'est pas vide
            gauche = self._afficher_sous_arbre(arbre.gauche, x - h, y + self.espacement_vert, h / 2) # Affiche le sous-arbre gauche
            droite = self._afficher_sous_arbre(arbre.droite, x + h, y + self.espacement_vert, h / 2) # Affiche le sous-arbre droit
            cercle = self.create_oval(x - self.diametre_cercle / 2, y, x + self.diametre_cercle / 2,
                                    y + self.diametre_cercle, fill="white", width=2) # Crée le cercle
            texte = self.create_text(x, y + self.diametre_cercle / 2,
                                    text=("{:.2%}".format(arbre.racine.valeur), arbre.racine.lettre if arbre.racine.lettre is not None else "")) # Crée le texte
            self.positions[arbre] = (x, y, cercle, texte) # Ajoute la position de l'arbre dans le dictionnaire
            if gauche is not None: # Si le sous-arbre gauche n'est pas vide
                angle = math.atan2(gauche[1] - (y + self.diametre_cercle / 2), gauche[0] - x) # Calcule l'angle de la ligne à tracer entre les deux sous-arbres (en radians)
                x1 = x + (self.diametre_cercle / 2) * math.cos(angle) # Calcule la position horizontale du point de départ
                y1 = (y + self.diametre_cercle / 2) + (self.diametre_cercle / 2) * math.sin(angle) # Calcule la position verticale du point de départ
                x2 = gauche[0] - (self.diametre_cercle / 2) * math.cos(angle) # Calcule la position horizontale du point d'arrivée
                y2 = gauche[1] + (self.diametre_cercle / 2) + (self.diametre_cercle / 2) * math.sin(angle) # Calcule la position verticale du point d'arrivée
                self.create_line(x1, y1, x2, y2, width=2) # Trace la ligne entre les deux sous-arbres
            if droite is not None: # Si le sous-arbre droit n'est pas vide
                angle = math.atan2(droite[1] - (y + self.diametre_cercle / 2), droite[0] - x) # Calcule l'angle de la ligne à tracer entre les deux sous-arbres (en radians)
                x1 = x + (self.diametre_cercle / 2) * math.cos(angle) # Calcule la position horizontale du point de départ
                y1 = (y + self.diametre_cercle / 2) + (self.diametre_cercle / 2) * math.sin(angle) # Calcule la position verticale du point de départ
                x2 = droite[0] - (self.diametre_cercle / 2) * math.cos(angle) # Calcule la position horizontale du point d'arrivée
                y2 = droite[1] + (self.diametre_cercle / 2) + (self.diametre_cercle / 2) * math.sin(angle) # Calcule la position verticale du point d'arrivée
                self.create_line(x1, y1, x2, y2, width=2) # Trace la ligne entre les deux sous-arbres
            return x, y # Retourne la position de l'arbre
        else: # Si l'arbre est vide
            return None # Retourne None

# PARTIE 2

# Question 2.1 - Calcule du pourcentage d'occurence de chaque lettre dans un texte.

def occurence(texte):
    occurence = dict()
    texte_list = list(texte.lower())
    while " " in texte_list:
        texte_list.remove(" ")
    for lettre in set(texte_list):
        occurence[lettre] = round((texte_list.count(lettre) / len(texte_list)), 2)
        #occurence[lettre] = "{0:.2%}".format(round((texte_list.count(lettre) / len(texte_list)), 4))
    return occurence

# Question 2.2 - Construction d'un arbre binaire de cryptage.

def construire_arbreB_Huffman(texte):
    """ 
    Construit un arbre binaire de cryptage à partir d'un texte. 
    :param texte: Le texte à crypter.
    :return: L'arbre binaire de cryptage.
    """
    # Création de la liste des sommets
    dict_occurence = occurence(texte)
    liste_sommets = []
    for lettre, occ in dict_occurence.items():
        liste_sommets.append(ArbreB(Sommet(occ, lettre)))
    liste_sommets.sort(key=lambda arbre: arbre.get_racine().valeur)
    # Construction de l'arbre de Huffman
    while len(liste_sommets) > 1:
        sommet_1 = min(liste_sommets, key=lambda arbre: arbre.get_racine().valeur)
        liste_sommets.remove(sommet_1)
        sommet_2 = min(liste_sommets, key=lambda arbre: arbre.get_racine().valeur)
        liste_sommets.remove(sommet_2)
        sommet_3 = ArbreB(Sommet(valeur=(sommet_1.get_racine().valeur + sommet_2.get_racine().valeur)),
                          sommet_1, sommet_2)
        liste_sommets.append(sommet_3)
        liste_sommets.sort(key=lambda arbre: arbre.get_racine().valeur)
    return liste_sommets[0]

def trouver_chemins_feuilles(arbre, chemin):
    """
    Trouve les chemins de toutes les feuilles d'un arbre de Huffman.
    :param arbre: L'arbre de Huffman.
    :param chemin: Le chemin suivi pour arriver au sommet actuel.
    :return: Un dictionnaire contenant les chemins des feuilles de l'arbre de Huffman.
    """
    if arbre is None:
        return {}
    if arbre.gauche is None and arbre.droite is None:
        return {arbre.racine.lettre: chemin}
    chemins = {}
    chemins.update(trouver_chemins_feuilles(arbre.gauche, chemin + [0]))
    chemins.update(trouver_chemins_feuilles(arbre.droite, chemin + [1]))
    return chemins

texte = "projetpython"
arbre = construire_arbreB_Huffman(texte)
chemins = trouver_chemins_feuilles(arbre, [])
print(chemins)

def test_construire_arbreB_Huffman():
    """
    Fonction de test de la fonction construire_arbreB_Huffman.
    """
    texte = "ProjetPython."
    print("Texte :")
    print(texte)
    print("Occurence des lettres :")
    print(occurence(texte))
    print("Arbre de Huffman :")
    print(construire_arbreB_Huffman(texte))

test_construire_arbreB_Huffman()

def test_interface_graphique_arbreB_Huffman():
    """
    Fonction de test de l'interface graphique.
    """
    # Création de la fenêtre
    fenetre = tk.Tk()
    fenetre.title("Arbre binaire de recherche")
    # Création de l'arbre binaire de recherche
    arbre = construire_arbreB_Huffman(texte)
    # Création de l'interface graphique
    interface_graphique = ArbreBinaire(fenetre, arbre, t=texte, width=800, height=600)
    interface_graphique.pack()
    interface_graphique.afficher()
    # Affichage de la fenêtre
    fenetre.mainloop()

test_interface_graphique_arbreB_Huffman()
