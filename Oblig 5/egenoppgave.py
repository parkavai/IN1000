
""" I denne egenoppgaven så tok jeg inspirasjon fra forslaget i oppgaveteksten.
Vi starter med å lage en tekstfil som består av de verdiene som ble nevnt i
oppgaveteksten. Derette skal vi hente denne tekstfilen og lage en ordbok av den
gjennom "funksjon". Videre benytter vi av funksjonen fra første deloppgaven uten
assert da det ikke var nødvendig siden verdiene allerede var over 0. Tilslutt
oppdaterer verdiene for hver nøkkelverdi ved å omgjøre tommer til cm og returnere
denne ordboken. """

textfil = open("tommer.txt")

ordboktommer = {}

def funksjon(filnavn):
    for i in filnavn:
        biter = i.split(" ")
        navn = biter[0]
        tommer = biter[1]
        ordboktommer[navn] = float(tommer)
    return(ordboktommer)

funksjon(textfil)

def tommerTilCM(antallTommer):
    for i in ordboktommer:
        tomtilcm = (ordboktommer[i]*2.54)
        ordboktommer.update({i: tomtilcm})
    return ordboktommer

print(tommerTilCM(ordboktommer))
