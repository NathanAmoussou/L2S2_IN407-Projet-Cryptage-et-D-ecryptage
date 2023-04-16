import tkinter as tk

class Sommet(object):
    def __init__(self, valeur, lettre=None):
        """
        Initialise un objet Sommet avec une valeur et une lettre optionnelle.
        :param valeur: La valeur du sommet.
        :param lettre: La lettre associée au sommet (optionnelle).
        """
        self.valeur = valeur
        self.lettre = lettre


class ArbreB(object):
    def __init__(self, racine, gauche=None, droite=None):
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
    
    def inserer_arbre(self, arbre):
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

    def supprimer_arbre(self, valeur):
        """
        Supprime un objet ArbreB avec une valeur donnée de l'arbre binaire de recherche.
        :param valeur: La valeur de l'objet ArbreB à supprimer de l'arbre binaire de recherche.
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

    def modifier_etiquette_arbre(self, valeur, nouvelle_valeur):
        """
        Modifie l'étiquette d'un objet ArbreB avec une valeur donnée dans l'arbre binaire de recherche.
        :param valeur: La valeur de l'objet ArbreB dont l'étiquette doit être modifiée.
        :param nouvelle_valeur: La nouvelle valeur à attribuer à l'étiquette de l'objet ArbreB.
        """
        if self.racine.valeur == valeur:
            self.racine.valeur = nouvelle_valeur
        elif valeur < self.racine.valeur and self.gauche is not None:
            self.gauche.modifier_etiquette_arbre(valeur, nouvelle_valeur)
        elif valeur > self.racine.valeur and self.droite is not None:
            self.droite.modifier_etiquette_arbre(valeur, nouvelle_valeur)

    def rechercher_element(self, valeur):
        """
        Recherche un objet ArbreB avec une valeur donnée dans l'arbre binaire de recherche.
        :param valeur: La valeur de l'objet ArbreB à rechercher dans l'arbre binaire de recherche.
        :return: L'objet ArbreB trouvé ou None si aucun objet ArbreB avec la valeur donnée n'est trouvé.
        """
        if self.racine.valeur == valeur:
            return self
        elif valeur < self.racine.valeur and self.gauche is not None:
            return self.gauche.rechercher_element(valeur)
        elif valeur > self.racine.valeur and self.droite is not None:
            return self.droite.rechercher_element(valeur)
        else:
            return None

    def __contains__(self, valeur):
        """
        Vérifie si une valeur donnée est contenue dans l'arbre binaire de recherche.
        :param valeur: La valeur à rechercher dans l'arbre binaire de recherche.
        :return: True si la valeur est trouvée dans l'arbre binaire de recherche, False sinon.
        """
        return self.rechercher_element(valeur) is not None

    def fusion(self, autre_arbre):
        """
        Fusionne cet arbre binaire de recherche avec un autre arbre binaire de recherche.
        :param autre_arbre: L'autre objet ArbreB à fusionner avec cet arbre binaire de recherche.
        """
        if autre_arbre is not None:
            self.inserer_arbre(ArbreB(autre_arbre.racine))
            self.fusion(autre_arbre.gauche)
            self.fusion(autre_arbre.droite)

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



