# Oppgave 1 og 2.)

""" Vi har en teller som er tallet bruker taster inn. Gjennon løkken,
vil alle verdiene som bruker taster inn, kjøre igjennom løkken frem til bruker
taster inn 0. Variabelen tall fungerer som en teller som skriver ut verdiene
bruker taster inn.  """

tall = 1

tomliste = []

while tall != 0:
    inp = input("Tast inn et heltall: ")
    tall = int(inp)
    tomliste.append(tall)
print("Du tastet 0, programmet avsluttes. \n")

tomliste.pop()

# Oppgave 3.)
print("Slik ser listen ut gjennom de verdiene du tastet inn: ")
for skriveutliste in tomliste:
    print(skriveutliste)

# Oppgave 4.)
minSum = 0
print("")
print("Summen av alle tallene i listen blir tilsammen: ")
for i in tomliste:
    minSum+=i
print(minSum)

# Oppgave 5 a.)

""" For å skrive ut det minste tallet, må vi ha en variabel som kalles minst.
Minst skal ha verdien til det første tallet i listen. For hver gang løkken kjøres,
kjøres en if-betingelse hvor minste_teller må ha en verdi mindre enn variabel
minst. Hvis betingelsen oppfylles, skal verdien til minst oppdateres til
minste_teller. Om det er flere verdier i listen som er mindre enn
minste_telleren, kjøres løkken flere ganger til det ikke er noen færre tall. """

print("")
print("Minste tallet i listen er: ")
minst = tomliste[0]
for minste_teller in tomliste:
    if minste_teller < minst:
        minst = minste_teller

print(minst)

# Oppgave 5 b.)

""" Samme prinsipp som forrige oppgave bare at vi gjør om på tegnet i
if-betingelsen. Hvis det ikke er noen større tall i listen, avslutter løkken. """

print("")
print("Største tallet i listen er: ")
stoerst = tomliste[0]
for stoerste_teller in tomliste:
    if stoerste_teller > stoerst:
        stoerst = stoerste_teller

print(stoerst)
