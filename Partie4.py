
def passage(case1,case2):
    

ok = True
assert passage((1,2),(2,2))==True , "erreur"
assert passage((2,2),(2,3))==False , "erreur"
assert passage((2,2),(3,3))==False , "erreur"
assert passage((2,2),(2,2))==False , "erreur"
assert passage((2,3),(2,5))==False , "erreur"
print('test ok', ok)
