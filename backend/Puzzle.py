from Bloc import Bloc
from Cellule import Cellule

class Puzzle:
    def __init__(self, initial, resolu):
        self.initial = initial
        self.resolu = resolu
        self.compteur = 0

    #scan le puzzle pour extraire les cellules vides
    def get_cellules_vides(self):
        cellules_vides = []
        # scan the whole puzzle for empty cells
        for ligne in range(9):
            for colonne in range(9):
                if self.resolu[ligne][colonne] == 0:
                    cellule = Cellule(ligne, colonne, 0)
                    cellules_vides.append(cellule)
        return cellules_vides


    def print_puzzle(self):
        for row in self.resolu:
            print(row)

    # enleve une valeur précise des cellules de la meme ligne, colonne et bloc
    def enleve_valeurs(self, cellule, valeurs_possibles):
        # indique que la cellule est déjà remplise
        valeurs_possibles[cellule.colonne + cellule.ligne * 9] = [0]

        # enleve la valeur des cellules de la meme ligne, colonne et bloc
        for x in valeurs_possibles[cellule.ligne * 9:cellule.ligne * 9 + 9]:
            try:
                x.remove(cellule.valeur)
            except ValueError:
                pass

        for i in range(9):
            try:
                valeurs_possibles[cellule.colonne + 9 * i].remove(cellule.valeur)
            except ValueError:
                pass

        block = Bloc(0, 0)
        block.set_blockx(cellule)
        block.set_blocky(cellule)

        for i in range(3):
            for j in range(3):
                try:
                    valeurs_possibles[block.x * 3 + j + (block.y* 3 + i) * 9].remove(cellule.valeur)
                except ValueError:
                    pass



        return valeurs_possibles

    #retourne les valeurs possibles pour chaque cellule
    def get_valeurs_possibles(self):

        valeurs_possibles = [[1,2,3,4,5,6,7,8,9] for i in range(81)]
        # initialize all remaining values to the full domain


        for ligne in range(9):
            for colonne in range(9):
                if self.resolu[ligne][colonne] != 0:
                    cellule = Cellule(ligne, colonne, self.resolu[ligne][colonne]);
                    valeurs_possibles = self.enleve_valeurs(cellule, valeurs_possibles)

        return valeurs_possibles

    # compte le nombre de foi
    # counts the number of times a value appears in constrained cells
    def get_lcv(self, valeurs, cellule, valeurs_possibles):
        lcv_list = []

        for valeur in valeurs:
            count = 0
            for i in range(9):
                if i == cellule.colonne:
                    continue
                x = valeurs_possibles[cellule.ligne * 9 + i]
                if valeur in x:
                    count += 1

            for i in range(9):
                if i == cellule.ligne:
                    continue
                x = valeurs_possibles[cellule.colonne + 9 * i]
                if valeur in x:
                    count += 1

            block = Bloc(0, 0)
            block.set_blockx(cellule)
            block.set_blocky(cellule)

            for i in range(3):
                for j in range(3):
                    if [block.y * 3 + i, block.x * 3 + j] == [cellule.ligne, cellule.colonne]:
                        continue
                    x = valeurs_possibles[block.x * 3 + j + (block.y  * 3 + i) * 9]
                    if valeur in x:
                        count += 1

            lcv_list.append(count)

        return lcv_list

    # retourner le nombre de cellule qui sont impacté par cette cellule (degree)
    def get_degree(self, cellule):
        degree = 0

        for i in range(9):
            if i == cellule.colonne:
                continue
            if self.resolu[cellule.ligne][i] == 0:
                degree += 1

        for i in range(9):
            if i == cellule.ligne:
                continue
            if self.resolu[i][cellule.colonne] == 0:
                degree += 1

        block = Bloc(0, 0)
        block.set_blockx(cellule)
        block.set_blocky(cellule)

        for i in range(3):
            for j in range(3):
                if [block.y* 3 + i, block.x * 3 + j] == [cellule.ligne, cellule.colonne]:
                    continue
                if self.resolu[block.y * 3 + i][block.x * 3 + j] == 0:
                    degree += 1

        return degree

    # vois si la valeur a enlever est la seule qui reste
    def forward_check(self, valeurs_possibles, valeur, cellule):
        for i in range(9):
            if i == cellule.colonne:
                continue

            x = valeurs_possibles[cellule.ligne * 9 + i]

            if len(x) == 1:
                if x[0] == valeur:
                    return 0

        for i in range(9):
            if i == cellule.ligne:
                continue

            x = valeurs_possibles[cellule.colonne + 9 * i]
            if len(x) == 1:
                if x[0] == valeur:
                    return 0

        block = Bloc(0, 0)
        block.set_blockx(cellule)
        block.set_blocky(cellule)

        for i in range(3):
            for j in range(3):

                if [block.y * 3 + i, block.x * 3 + j] == [cellule.ligne, cellule.colonne]:
                    continue

                x = valeurs_possibles[block.x * 3 + j + (block.y * 3 + i) * 9]
                if len(x) == 1:
                    if x[0] == valeur:
                        return 0
        return 1

    def resoudre(self):
        # liste des cellules vides qui restes
        self.compteur = self.compteur +1
        cellules_vides = self.get_cellules_vides()

        # si il ne reste plus aucune cellule vide
        if len(cellules_vides) == 0:
            self.print_puzzle()
            return 1

        # trouvé la cellule qui contient le moins de valeurs possibles
        valeurs_possibles = self.get_valeurs_possibles()
        mrv_list = []
        [mrv_list.append(len(valeurs_possibles[cellule.ligne * 9 + cellule.colonne])) for cellule in cellules_vides]
        # liste des cellules qui ont le moins valeurs possibles (mrv : minimum remaining values)
        mrv_squares = []
        minimum = min(mrv_list)
        for i in range(len(mrv_list)):
            valeur = mrv_list[i]
            if valeur == minimum:
                mrv_squares.append(cellules_vides[i])


        # si il ne reste qu'une cellule
        if len(mrv_squares) == 1:
            cellule = mrv_squares[0]
        else:
            # sinon, trouvé cellule qui pose le plus de contrainte(plus grand degree)
            degree_list = []
            for cell in mrv_squares:
                degree = self.get_degree(cell)
                degree_list.append(degree)
                max_degree = max(degree_list)
                max_degree_squares = []
                for i in range(len(degree_list)):
                    valeur = degree_list[i]
                    if valeur == max_degree:
                        max_degree_squares.append(mrv_squares[i])
                # prendre la première cellule
                cellule = max_degree_squares[0]

        valeurs = valeurs_possibles[cellule.colonne + cellule.ligne * 9]

        while len(valeurs) != 0:

            lcv_list = self.get_lcv(valeurs, cellule, valeurs_possibles)
            # prendre celle qui possede la valeur la moins contraignante
            # take the least constraining value
            valeur = valeurs[lcv_list.index(min(lcv_list))]
            valeurs.remove(valeur)

            if self.forward_check(valeurs_possibles, valeur, cellule):
                self.resolu[cellule.ligne][cellule.colonne] = valeur
                if self.resoudre():
                    return 1
                else:
                    self.resolu[cellule.ligne][cellule.colonne] = 0

        return 0




