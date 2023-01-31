def forekommer(liste, tall):
    if tall in liste:
        return True
    return False

def sameSet(liste_a, liste_b):
    sjekk = False
    for x in liste_a:
        if(forekommer(liste_b, x) == True):
            sjekk = True
        else:
            return False
    for y in liste_b:
        if(forekommer(liste_a, y) == True):
            sjekk = True
        else:
            return False
    return sjekk

print(sameSet([1,4,9,16,9,7,4,9,11], [11, 11, 7, 9, 16, 4, 1]))
                
