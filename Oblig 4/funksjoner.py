# Oppgave 1.)

def adder(tall1,tall2):
    return tall1 + tall2

print("Tallene 4 og 5 tilsvarer " + str(adder(4,5)))
print("Tallene 3 og 4 tilsvarer " + str(adder(3,4)))
print("")
# Oppgave 2.)

""" Lager tre variabler tekststreng, bokstav og en teller for denne oppgaven.
Gjennom en for-løkke, går vi gjennom stringen. Vi lager en if-betingelse hvor
telleren ser om bokstaven bruker har tastet inn, ligger i tekstrengen. Oppfylles
betingelsen, skal telleren øke med 1. Telleren sin funksjon er å telle antall
ganger den gitte bokstaven befinner seg i tekstrengen. Deretter skriver vi ut
antall forekomster av det bokstavet i tekstrengen."""

inp = input("Skriv inn en string: ")

tekststreng = inp

inp2 = input("Skriv inn et bokstav: ")

bokstav = inp2

teller = 0

# Oppgave 3.)

print("")
def tellminforekomst(minBokstav,minTekst):
    teller = 0
    for i in minTekst:
        if i == minBokstav:
            teller +=1
    print ("Antall forekomster av bokstaven " + bokstav + " tilsvarer: " + str(teller))

tellminforekomst(bokstav,tekststreng)
