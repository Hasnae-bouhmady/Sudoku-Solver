from Cellule import Cellule
class Bloc:

    def __init__(self, id1, id2):
        self.x = id1
        self.y = id2

    def set_blockx(self, cellule):

        if cellule.colonne <= 2 and cellule.colonne >= 0:
            self.x = 0
        else:
            if cellule.colonne <= 5 and cellule.colonne >= 3:
                self.x = 1
            else:
                self.x = 2

    def set_blocky(self, cellule):
        if cellule.ligne <= 2 and cellule.ligne >= 0:
            self.y = 0
        else:
            if cellule.ligne <= 5 and cellule.ligne >= 3:
                self.y = 1
            else:
                self.y = 2