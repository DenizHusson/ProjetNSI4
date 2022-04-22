import turtle


# À faire : création d'une erreur personnalisée pour les besoins de la classe


class Graphe():
    """
    Objet représentant un multigraphe non orienté à l'aide d'un dictionnaire
    associant à chacun des sommets du graphe un ensemble de ses voisins. Chaque
    sommet est représenté par un couple en tuple, correspondant aux coordonnées
    strictement positives du sommet.
    Attributs:
        dico: dict, un dictionnaire des sommets voisins
    """
    # À faire : le graphe ne peut pas contenir de boucles, ni d'arêtes
    # multiples. Il est possible de prévenir les boucles (seulement si le coût
    # n'est pas plus grand).

    # À faire : possibilité de faire des labyrinthes non rectangles ?

    # Constantes de classe
    DEPARTX = -320
    DEPARTY = 250

    def __init__(self) -> None:
        """
        Crée un objet graphe vide.
        Préconditions: Aucune
        Postconditions:
            Création d'un objet graphe vide, avec un dico vide.
        """
        self.dico = {}

    def __str__(self) -> str:
        """
        Renvoie pour la représentation en string la représentation du dico de
        l'objet.
        Préconditions: Aucune
        Postconditions:
            Renvoie:
                _: str, la représentation du dico de l'objet
        """
        return str(self.dico)

    def addSommet(self, sommet: tuple) -> None:
        """
        Ajoute au graphe un nouveau sommet s'il n'existe pas. Sinon, ne fait
        rien.
        Préconditions:
            Arguments:
                sommet: tuple, un couple représentant les coordonnées du sommet
        """
        if sommet not in self.dico:
            self.dico[sommet] = set()

    def addArete(self, sa: tuple, sb: tuple) -> None:
        """
        Ajoute une nouvelle arête au graphe entre un ou deux sommets. Plusieurs
        arêtes peuvent exister entre deux mêmes sommets.
        Préconditions:
            Les deux sommets précisés doivent avoir été ajoutés au graphe.
            Arguments:
                sa: tuple, l'un des sommets du graphe
                sb: tuple, l'un des sommets du graphe
        Postconditions:
            Ajout d'une arête entre les deux sommets précisés.
        Erreurs:
            SommetInexistantErreur: si l'une des arêtes n'existe pas
        """
        self.dico[sa].add(sb)
        self.dico[sb].add(sa)
        # À faire : ajouter une vérification de l'existence des arêtes, en
        # récupérant d'abord les listes avec .get

    def _placementOrigine(self):
        """
        Replace turtle en haut à droite du dessin, et le refait pointer vers la
        droite, pinceau levé.
        Préconditions:
            Un environnement graphique doit permettre de dessiner dans une
            fenêtre le labyrinthe.
        Postconditions:
            Replacement de turtle.
        """
        turtle.up()
        turtle.goto(Graphe.DEPARTX, Graphe.DEPARTY)
        turtle.setheading(0)

    def _limites(self, besoins: int) -> (int, int, float):
        """
        Renvoie les lignes et les colonnes que constitue le graphe si il
        représente bien un labyrinthe rectangle. Les informations non demandées
        auront pour valeur 0.
        Préconditions:
            Le graphe doit bien représenter un graphe rectangle.
            Arguments:
                besoins: int, une bitmap représentant les besoins
                    4 représente le nombre de lignes
                    2 représente le nombre de colonnes
                    1 représente le côté des cases
        Postconditions:
            Renvoie:
                tuple, un tuple de trois valeurs, contenant la valeur requise ou
                0 si la valeur n'était pas requise.
        """
        nbli = 0
        nbcol = 0
        # À faire : améliorer le calcul de la distance potentielle renvoyée
        dist = 50
        if besoins & 4:
            nbli = max([elt[0] for elt in self.dico.keys])
        if besoins & 2:
            nbcol = max([elt[1] for elt in self.dico.keys])
        # À faire : réimplanter pour une meilleure efficacité
        return (nbli,nbcol,dist)

    def showLabyrinthe(self, nbli: int = None, nbcol: int = None, dist: float \
            = None) -> None:
        """
        Dessine avec le module turtle le labyrinthe correspondant au graphe, en
        suivant les information données sur les dimensions du labyrinthe.
        Préconditions:
            Le graphe doit contenir tous les sommets constituant la grille nbli
            X nbcol.
            Un environnement graphique doit permettre de dessiner dans une
            fenêtre le labyrinthe.
            Arguments:
                nbli: int, le nombre de lignes du labyrinthe. Par défaut, la
                plus grande ordonnée trouvée dans le graphe.
                nbcol: int, le nombre de colonnes du labyrinthe. Par défaut, la
                plus grande abscisse trouvée dans le graphe.
                dist: float, le côté d'une case de la grille. Par défaut une
                valeur de 50.
        Postconditions:
            Apparition à l'écran du labyrinthe.
        """
        besoins = 0
        if nbli is None: besoins+=4
        if nbcol is None: besoins+=2
        if dist is None: besoins+=1
        dimensions = self._limites(besoins)
        if nbli is None: nbli = dimensions[0]
        if nbcol is None: nbli = dimensions[1]
        if dist is None: nbli = dimensions[2]

        self._cadre(nbli,nbcol,dist)
        self._paroisVerticales(nbli,nbcol,dist)
        self._paroisHorizontales(nbli,nbcol,dist)

    def _cadre(self, nbli: int, nbcol: int, dist: float) -> None:
        """
        Dessine un cadre au labyrinthe représenté par le graphe, selon un nombre
        de lignes, colonnes, et un côté des cases.
        Préconditions:
            Un environnement graphique doit permettre d'utiliser turtle.
            Arguments:
                nbli: int, le nombre de lignes du labyrinthe dont on dessine le
                cadre.
                nbcol: int, le nombre de colonnes du labyrinthe dont on dessine le
                cadre.
        Postconditions:
            Dessine un cadre pour afficher le labyrinthe représenté par le
            graphe.
        """
        self._placementOrigine()
        turtle.down()
        for _ in range(2):
            turtle.forward(dist*nbcol)
            turtle.right(90)
            turtle.forward(dist*nbli)
            turtle.right(90)

    def _paroisVerticales(self, nbli: int, nbcol: int, dist: int):
        """
        Dessine les parois verticales du labyrinthe représenté par le graphe,
        selon un nombre de lignes, colonnes, et un côté des cases.
        Préconditions:
            Le graphe doit contenir tous les points dans lesquels passe le
            dessin selon les dimensions données.
            Un environnement graphique doit permettre d'utiliser turtle.
            Arguments:
                nbli: int, le nombre de lignes du labyrinthe dont on dessine
                les parois verticales.
                nbcol: int, le nombre de colonnes du labyrinthe dont on dessine
                les parois verticales.
        Postconditions:
            Dessine les bordures verticales du labyrinthe représenté par le
            graphe.
        """
        # À faire : ajouter un error check avec .get() pour éviter une valeur
        # inexistante
        self._placementOrigine()
        for ligne in range(1, nbli+1):
            for colonne in range(1, nbcol):
                # Pas besoin de passer sur la dernière case des lignes pour dessiner
                turtle.forward(dist)
                if (ligne, colonne+1) not in self.dico[(ligne,colonne)]:
                    # Dessine s'il n'y a pas de liaison entre cases voisines
                    turtle.right(90)
                    turtle.down()
                    turtle.forward(dist)
                    turtle.up()
                    turtle.backward(dist)
                    turtle.left(90)
            turtle.backward((nbcol-1)*dist) # Retour en début de ligne
            turtle.right(90)
            turtle.forward(dist) # Descente d'une ligne
            turtle.left(90) # Réorientation

    def _paroisHorizontales(self, nbli: int, nbcol: int, dist: int):
        """
        Dessine les parois horizontales du labyrinthe représenté par le graphe,
        selon un nombre de lignes, colonnes, et un côté des cases.
        Préconditions:
            Le graphe doit contenir tous les points dans lesquels passe le
            dessin selon les dimensions données.
            Un environnement graphique doit permettre d'utiliser turtle.
            Arguments:
                nbli: int, le nombre de lignes du labyrinthe dont on dessine
                les parois horizontales.
                nbcol: int, le nombre de colonnes du labyrinthe dont on dessine
                les parois horizontales.
        Postconditions:
            Dessine les bordures horizontales du labyrinthe représenté par le
            graphe.
        """
        # À faire : ajouter un error check avec .get() pour éviter une valeur
        # inexistante
        self._placementOrigine()
        turtle.right(90) # Placement dans le sens vertical
        for colonne in range(1, nbcol+1):
            for ligne in range(1, nbli):
                # Pas besoin de passer sur la dernière case des lignes pour dessiner
                turtle.forward(dist)
                if (ligne+1, colonne) not in self.dico[(ligne,colonne)]:
                    # Dessine s'il n'y a pas de liaison entre cases voisines
                    turtle.left(90)
                    turtle.down()
                    turtle.forward(dist)
                    turtle.up()
                    turtle.backward(dist)
                    turtle.right(90)
            turtle.backward((nbli-1)*dist) # Retour en début de ligne
            turtle.left(90)
            turtle.forward(dist) # Descente d'une ligne
            turtle.right(90) # Réorientation

    def drawGraph(self) -> None:
        """
        Affiche à l'écran le labyrinthe représenté par le graphe ainsi que ses noeuds 
        et chemins à l'aide du module turtle, en admettant que celui-ci
        représente un labyrinthe rectangulaire.
        Chaque noeud est représenté par un cercle, et les chemins sont
        représentés par des segments horizontaux ou verticaux reliant les
        cercles.
        Préconditions:
            Le graphe doit représenter un labyrinthe rectangulaire.
            Un environnement graphique doit être disponible.
        Postconditions:
            Dessin à l'écran du labyrinthe et de ses noeuds, avec les chemins
            les reliant.
        """
        # À faire : Proposer des arguments du même type que showLabyrinthe()
        #   pour plus de flexibilité, au moins sur le côté
        self.showLabyrinthe()
        # Dessine les noeuds sous forme de rond
        self._placementOrigine()
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(45)
        turtle.left(90)
        for _ in range():
            turtle.circle(20)

        self.cheminsHorizontaux()
        self.cheminsVerticaux()


# Constantes générales
HORIZONTALE = 8
VERTICALE = 4


LstSommet = Graphe()

for counta in range(1, VERTICALE+1):
    for countb in range(1, HORIZONTALE+1):
        LstSommet.addSommet((counta,countb))

aretes = [
        [(1,1),(2,1)],
        [(2,1),(2,2)],
        [(2,2),(3,2)],
        [(3,2),(4,2)],
        [(4,2),(4,3)],
        [(4,3),(4,4)],
        [(2,2),(2,3)],
        [(2,3),(1,3)],
        [(1,3),(1,4)],
        [(1,4),(2,4)],
        [(1,4),(1,5)],
        [(2,4),(3,4)],
        [(3,4),(3,5)],
        [(3,5),(3,6)],
        [(3,6),(4,6)],
        [(4,6),(4,5)],
        [(3,6),(3,7)],
        [(3,7),(4,7)],
        [(4,7),(4,8)],
        [(3,8),(4,8)],
        [(2,8),(3,8)],
        [(2,8),(1,8)],
        [(1,7),(1,8)],
        [(1,7),(1,6)],
        [(2,6),(1,6)],
        [(2,6),(3,6)],
        [(2,6),(2,7)],
        [(3,7),(2,7)],
        [(1,4),(1,5)],
        [(2,5),(1,5)],
        [(2,5),(2,6)],
        ]

for arete in aretes:
    LstSommet.addArete(arete[0],arete[1])

print(LstSommet)
LstSommet.showLabyrinthe(VERTICALE, HORIZONTALE, 50)
