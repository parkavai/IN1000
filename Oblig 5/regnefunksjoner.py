# Oppgave 1.)

""" Lager en funksjon kalt "addisjon" som returnerer summen av verdiene
lagt til i parameteren. I tillegg en assert som sjekker om summen tilsvarer
resultatet av verdiene plusset med hverandre.  """

def addisjon(add1,add2):
    sum = add1+add2
    return sum

Summen = addisjon(5,4)
print(Summen)
assert Summen == 9, "Addisjon mellom 5 og 4 skal gi 9"


# Oppgave 2.)


""" Samme fremgangsmåte som den forrige oppgaven, men at vi skal ha funksjoner
for subtraksjon og deling. """

print("")
def subtraksjon(sub1,sub2):
    forskjell = sub1-sub2
    return forskjell

Forskjellen = subtraksjon(5,4)
print(Forskjellen)
assert Forskjellen == 1, "Subtraksjon mellom 5 og 4 skal gi 1"

print("")
def divisjon(div1,div2):
    deling = div1/div2
    return deling

Delingen = divisjon(8,4)
print(Delingen)
assert Delingen == 2, "Divisjon mellom 8 og 4 skal gi 2"

# Oppgave 3.)

def tommerTilCM(antallTommer):
    assert antallTommer > 0
    tomtilcm = (antallTommer*2.54)
    return tomtilcm

# Oppgave 4.)

""" Bruker samme utskriftsformat som vist i oppgaveteksten. """

print()
print("Utregninger: ")
def skrivBeregninger():
    inp1 = float(input("Skriv inn tall 1: "))
    inp2 = float(input("Skriv inn tall 2: "))
    Summen = addisjon(inp1,inp2)
    Forskjellen = subtraksjon(inp1,inp2)
    Delingen = divisjon(inp1,inp2)
    print("Resultatet av summering: ", str(Summen))
    print("Resultatet av Subtraksjon: ", str(Forskjellen))
    print("Resultatet av Delingen: ", str(Delingen))
    print("")
    print("Konvertering fra tommer til cm: ")
    inp3 = float(input("Skriv inn et tall: "))
    Tommeren = tommerTilCM(inp3)
    print("Resultat: ", str(Tommeren))

skrivBeregninger()
