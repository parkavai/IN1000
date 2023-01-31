def lesInnFil(filnavn):
    fil = open(filnavn, "r")
    ordbok = {}
    for linje in fil:
        data = linje.strip().split(",")
        navn = data[0]
        karakter = data[1]
        listeAvNavn = [navn]
        if karakter not in ordbok.keys():
            ordbok[karakter] = listeAvNavn
        else:
            ordbok.get(karakter).append(navn)
    fil.close()
    return ordbok

lesInnFil("karakterer.txt")

def hent_vanligste_karakter(karakterordbok):
    stoerste = 0
    karakteren = ""
    for x in karakterordbok:
        if (stoerste < len(karakterordbok[x])):
            stoerste = len(karakterordbok[x])
            karakteren = x
    return karakteren

print(hent_vanligste_karakter(lesInnFil("karakterer.txt")))


        
        
