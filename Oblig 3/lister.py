# Oppgave 1)

# Lag er en liste med verdiene 1,2 og 3.

liste = [1,2,3]

# Legger til verdien 4 gjennom append.

liste.append(4)

# For å printe ut første og tredje verdi så skriver vi inn tallet for
# rekkefølgen tallet er plassert i lista.

print(liste[0], liste[2])

# Oppgave 2.)

# Lager en liste med navnet tomliste.

tomliste = []

# Lager input-felt for de 4 navnene som bruker skal taste inn.

inp1 = input("Skriv inn et navn: ")

inp2 = input("Skriv inn et nytt navn: ")

inp3 = input("Skriv inn enda et nytt navn: ")

inp4 = input("Skriv inn det siste navnet du kommer på : ")

# Legger til variablene i listen.

tomliste = [inp1, inp2, inp3, inp4]

# Kjører en if-sjekk som sjekker om navnet mitt "Parkavan" er skrevet i listen.
""" For å sjekke om navnet er i listen, brukes funksjonen "in" som bekrefter
om noen av navnene som bruker tastet, tilsvarer mitt navn.
"""

if "Parkavan" in tomliste:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

# Oppgave 4.)

# Lager to variabler hvor den ene heter sum mens den andre heter produkt.

sum = (1+2+3+4)

produkt = (1*2*3*4)

# Lager en liste kun med disse variablene

nyliste = [sum, produkt]

# Slår sammen den første og den nye listen

tilsammenliste = nyliste + liste

# Bruker funksjonen pop 2 ganger til å fjerne de siste elementene i lista

tilsammenliste.pop()

tilsammenliste.pop()

print(tilsammenliste)
