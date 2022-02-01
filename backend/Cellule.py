class Cellule:

    def __init__(self, Ligne, Colonne, Valeur):
        self.ligne = Ligne
        self.colonne = Colonne
        self.valeur = Valeur

    def set_valeur(self, i):
        self.valeur = i