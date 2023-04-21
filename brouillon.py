import tkinter as tk

class Sommet:
    def __init__(self, valeur: float, lettre: str=None):
        self.valeur = valeur
        self.lettre = lettre

class ArbreB:
    def __init__(self, racine: Sommet, gauche=None, droite=None):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite

def dessiner_arbre(arbre, x, y, dx):
    if arbre is not None:
        canvas.create_text(x, y, text=str(arbre.racine.valeur))
        if arbre.gauche is not None:
            x0 = x - dx
            y0 = y + 60
            canvas.create_line(x, y, x0, y0)
            dessiner_arbre(arbre.gauche, x0, y0, dx/2)
        if arbre.droite is not None:
            x1 = x + dx
            y1 = y + 60
            canvas.create_line(x, y, x1, y1)
            dessiner_arbre(arbre.droite, x1, y1, dx/2)

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()

# Exemple d'arbre binaire
a = Sommet(1)
b = Sommet(2)
c = Sommet(3)
d = Sommet(4)
e = Sommet(5)
f = Sommet(6)
g = Sommet(7)

arbre = ArbreB(a,
               ArbreB(b,
                      ArbreB(d),
                      ArbreB(e)),
               ArbreB(c,
                      ArbreB(f),
                      ArbreB(g)))

dessiner_arbre(arbre, 200, 30, 100)

root.mainloop()