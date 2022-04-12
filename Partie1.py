from turtle import *

class graph() :
    def __init__(self) :
        self.dico = {}

    def __str__(self):
        return str(self.dico)

    def addSommet(self,sommet):
        if sommet not in self.dico:
            self.dico[sommet] = []

    def addArete(self,sa,sb) :
        self.dico[sa].append(sb)
        self.dico[sb].append(sa)

def showLabyrinthe(nbli,nbcol,dist):
    cadre(nbli,nbcol,dist)
    paroisVerticales(nbli,nbcol,dist)
    paroisHorizontales(nbli,nbcol,dist)


LstSommet = graph()

horizontale = 8
verticale = 4
counta = 1
countb = 1

for i in range(verticale):
    for j in range(horizontale):
        LstSommet.addSommet((counta,countb))
        countb+=1
    counta+=1
    countb = 1

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
        [(2,5),(2,6)]]

for i in arretes:
    LstSommet.addArete(i[0],i[1])

print(LstSommet)


