def les_tall_fra_fil(filnavn):
    fil = open(filnavn, "r")
    tall_liste = []
    for linje in fil:
        tall_liste.append(int(linje))
    return tall_liste

def antall_forekomster(liste, tall):
    teller = 0
    for x in liste:
        if(x == tall):
            teller += 1
    return teller

def flest_forekomster(liste):
    stoerste = 0
    tallet = 0
    for x in liste:
        if (stoerste < antall_forekomster(liste, x)):
            stoerste = antall_forekomster(liste, x)
            tallet = x
    return tallet

print(flest_forekomster(les_tall_fra_fil("tallene.txt")))