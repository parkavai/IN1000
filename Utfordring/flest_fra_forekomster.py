def les_fra_fil(filnavn):
    fil = open(filnavn, "r")
    liste = []
    for linje in fil:
        liste.append(int(linje))
    return liste 

les_fra_fil("fil_tall.txt")

def antall_forekomster(liste, heltall):
    antForekomster = 0
    for tall in liste:
        if(tall == heltall):
            antForekomster += 1
    return antForekomster

def flest_forekomster(liste):
    flestForekomst = 0
    teller = 0
    for tall in liste:
        if(antall_forekomster(liste, tall) > teller):
            teller = antall_forekomster(liste, tall)
            flestForekomst = tall 
    return flestForekomst

print(flest_forekomster(les_fra_fil("fil_tall.txt")))

