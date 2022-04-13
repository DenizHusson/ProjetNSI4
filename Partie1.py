from turtle import *


# À faire : création d'une erreur personnalisée pour les besoins de la classe


class Graph():
    """
    Objet représentant un multigraphe non orienté à l'aide d'un dictionnaire
    associant à chacun des sommets du graphe ses voisins. Chaque sommmet est
    représenté par un couple en tuple, correspondant aux coordonnées du sommet.
    Attributs:
        dico: dict, un dictionnaire des sommets voisins
    """
    # À faire : le graphe ne peut pas contenir de boucles, ni d'arêtes
    # multiples. Il est possible de prévenir les boucles (seulement si le prix
    # n'est pas plus grand) ou d'utiliser des ensembles pour les voisins d'un
    # sommet.

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
            self.dico[sommet] = []

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
        self.dico[sa].append(sb)
        self.dico[sb].append(sa)
        # À faire : ajouter une vérification de l'existance des arêtes, en
        # récupérant d'abord les listes avec .get

    def showLabyrinthe(self, nbli: int, nbcol: int, dist: float) -> None:
        """
        Dessine avec le module turtle le labyrinthe correspondant au graphe, en
        suivant les information données sur les dimensions du labyrinthe.
        Préconditions:
            Le graphe doit contenir tous les sommets constituant la grille nbli
            X nbcol.
            Un environnement graphique doit permettre de dessiner dans une
            fenêtre le labyrinthe.
            Arguments:
                nbli: int, le nombre de lignes du labyrinthe
                nbcol: int, le nombre de colonnes du labyrinthe
                dist: float, le côté d'une case de la grille
        Postconditions:
            Apparition à l'écran du labyrinthe.
        """
        # À faire : ajout éventuel d'erreurs pour divers cas

        self.cadre(nbli,nbcol,dist)
        self.paroisVerticales(nbli,nbcol,dist)
        self.paroisHorizontales(nbli,nbcol,dist)

    def cadre(self, nbli: int, nbcol: int, dist: float) -> None:
        pass

# Constantes générales
HORIZONTALE = 8
VERTICALE = 4


LstSommet = Graph()

for counta in range(1, VERTICALE+1):
    for countb in range(1, HORIZONTALE+1):
        LstSommet.addSommet((counta,countb))

arretes = [
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

for arrete in arretes:
    LstSommet.addArete(arrete[0],arrete[1])

print(LstSommet)
