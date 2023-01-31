def equals(liste_en, liste_to):
    peker = 0 
    if(len(liste_en) != len(liste_to)):
        return False 
    while(peker < len(liste_en) - 1):
        if(liste_en[peker] != liste_to[peker]):
            return False 
        peker += 1
    return True 

print(equals([1,2,3],[1,2,3]))

def sameSet(liste_a, liste_b):
    for x in liste_a:
        if (x not in liste_b):
            return False 
    for y in liste_b:
        if(y not in liste_a):
            return False 
    return True 

print(sameSet([1,4,9,16,9,7,4,9,11], [11,11,7,9,16,4,1]))