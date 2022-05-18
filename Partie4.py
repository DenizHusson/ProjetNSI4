
def passage(case1,case2,LstSommet):
    for valeur in LstSommet[case1]:
        if valeur == case2:
            return True    
    return False

ok = True
assert passage((1,2),(2,2))==True , "erreur"
assert passage((2,2),(2,3))==False , "erreur"
assert passage((2,2),(3,3))==False , "erreur"
assert passage((2,2),(2,2))==False , "erreur"
assert passage((2,3),(2,5))==False , "erreur"
print('test ok', ok)
