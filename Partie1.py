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

LstSommet.addArete((1,1),(2,1))
LstSommet.addArete((2,1),(2,2))
LstSommet.addArete((2,2),(3,2))
LstSommet.addArete((3,2),(4,2))
LstSommet.addArete((4,2),(4,3))
LstSommet.addArete((4,3),(4,4))

LstSommet.addArete((2,2),(2,3))
LstSommet.addArete((2,3),(1,3))
LstSommet.addArete((1,3),(1,4))
LstSommet.addArete((1,4),(2,4))
LstSommet.addArete((1,4),(1,5))
LstSommet.addArete((2,4),(3,4))
LstSommet.addArete((3,4),(3,5))
LstSommet.addArete((3,5),(3,6))
LstSommet.addArete((3,6),(4,6))
LstSommet.addArete((4,6),(4,5))

LstSommet.addArete((3,6),(3,7))
LstSommet.addArete((3,7),(4,7))
LstSommet.addArete((4,7),(4,8))
LstSommet.addArete((3,8),(4,8))
LstSommet.addArete((2,8),(3,8))
LstSommet.addArete((2,8),(1,8))
LstSommet.addArete((1,7),(1,8))
LstSommet.addArete((1,7),(1,6))
LstSommet.addArete((2,6),(1,6))
LstSommet.addArete((2,6),(3,6))
LstSommet.addArete((2,6),(2,7))
LstSommet.addArete((3,7),(2,7))

LstSommet.addArete((1,4),(1,5))
LstSommet.addArete((2,5),(1,5))
LstSommet.addArete((2,5),(2,6))

print(LstSommet)
