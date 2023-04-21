import tkinter as tk
from main import *
from math import atan2, cos, sin

sommet_a = Sommet(8, "A")
sommet_b = Sommet(2, "B")
sommet_c = Sommet(7, "C")
arbre1 = ArbreB(sommet_a)
arbre1 += ArbreB(sommet_b)
arbre1 += ArbreB(sommet_c)
arbre1 += ArbreB(Sommet(1, "D"))
arbre1 += ArbreB(Sommet(8, "E"))
arbre1 += ArbreB(Sommet(6, "F"))
arbre1 += ArbreB(Sommet(8, "G"))
arbre1 += ArbreB(Sommet(0, "H"))
arbre1 += ArbreB(Sommet(4, "I"))
arbre1 += ArbreB(Sommet(9, "J"))


test_construire_arbreB_Huffman()

arbre2 = construire_arbreB_Huffman("Projet Python")

class GUI2(tk.Canvas):
    def __init__(self, master, arbre, *args, **kwargs):
        tk.Canvas.__init__(self, master, *args, **kwargs)
        self.arbre = arbre
        self.width = 1000
        self.height = 375
        self.diametre_cercle = 80
        self.espacement_horiz = 8
        self.espacement_vert = 50
        self.positions = {}

    def afficher(self):
        self.delete(tk.ALL)
        self.positions.clear()
        self._afficher_sous_arbre(self.arbre, self.width / 2, 10, self.width / 4)
    
    def _afficher_sous_arbre(self, arbre, x, y, h):
        offset = 17
        if arbre is not None:
            gauche = self._afficher_sous_arbre(arbre.gauche, x - h, y + self.espacement_vert, h / 2)
            droite = self._afficher_sous_arbre(arbre.droite, x + h, y + self.espacement_vert, h / 2)
            texte = self.create_text(x, y + self.diametre_cercle / 2, text=("{:.0%}".format(arbre.racine.valeur)))
            if arbre.racine.lettre is not None:
                texte = self.create_text(x, y + self.diametre_cercle / 2 + 15, text=arbre.racine.lettre)
            self.positions[arbre] = (x, y, texte)
            if gauche is not None:
                angle = atan2(gauche[1] - y - self.diametre_cercle / 2, gauche[0] - x)
                x1 = x + offset * cos(angle)
                y1 = y + self.diametre_cercle / 2 + offset * sin(angle)
                x2 = gauche[0] - offset * cos(angle)
                y2 = gauche[1] + self.diametre_cercle / 2 - offset * sin(angle)
                self.create_line(x1, y1, x2, y2, width=2)
            if droite is not None:
                angle = atan2(droite[1] - y - self.diametre_cercle / 2, droite[0] - x)
                x1 = x + offset * cos(angle)
                y1 = y + self.diametre_cercle / 2 + offset * sin(angle)
                x2 = droite[0] - offset * cos(angle)
                y2 = droite[1] + self.diametre_cercle / 2 - offset * sin(angle)
                self.create_line(x1, y1, x2, y2, width=2)
            return x, y
        else:
            return None

GUI = GUI2(tk.Tk(), arbre2)
GUI.place(x=500, y=187.5, width=1000, height=375, anchor="center")  # modification ici
GUI.afficher()
GUI.mainloop()
