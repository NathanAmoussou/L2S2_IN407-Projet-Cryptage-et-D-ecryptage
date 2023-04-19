texte = "projetpython"
dictionnaire = {'p': [0, 0], 't': [0, 1], 'r': [1, 0, 0, 0], 'j': [1, 0, 0, 1], 'n': [1, 0, 1, 0], 'h': [1, 0, 1, 1], 'y': [1, 1, 0, 0], 'e': [1, 1, 0, 1], 'o': [1, 1, 1]}
mot_binaire = ''.join([str(chiffre) for lettre in texte for chiffre in dictionnaire[lettre]])
print(mot_binaire)