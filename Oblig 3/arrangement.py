""" Jeg har tatt inspirasjon fra ett av foreslagene for oppgaven, nemlig å
lage et arrangement som skal ha oversikt over matvarer som kan trigge ulike
allergier. Først skal bruker få oversikt over de allergiene som er blitt skrevet
i systemet. Deretter taste inn allergien for å se ann hvilke matvarer som utløser
allergien. Her har jeg brukt liste, prosedyre og ordbok for denne oppgaven.
"""

# Lister over de ulike allergiene.

noetter = ["peanøtter", "mandler", "cashew-nøtter", "pistasj-nøtter"]

skalldyr = ["rekechips", "fiskeretter", "marinader", "salater"]

gluten = ["brød", "kaker", "kjeks", "pizza", "kornblandinger"]

# Ordbok for som har navnet på allergien som nøkkelverdi og matvarene som verdier.

allergier = {"noetter": noetter,"skalldyr": skalldyr,"glutenallergi": gluten}

# En melding for deltakere om arrangement og matvarer.

print(""" For dette arrangementet så har vi lagd et program som holder oversikt
over matvarer som bør unngås for deltakere som strever med allergier. """)

liste_over_allergier = ["noetter", "skalldyr", "gluten"]

""" Skriver ut de ulike allergiene. Om bruker taster inn et allergi, kjøres
en if-sjekk som sjekker om allergien brukeren har tastet inn, er i systemet.
Hvis ikke får de en beskjed om at listen skal oppdateres. """

def allergi():
    print("Her er en liste med allergiene som vi har listet foreløping: ", liste_over_allergier)
    inp = input("Skriv inn ditt allergi: ")
    allergi = inp
    if allergi in allergier:
        print("Her er matvarene som bør unngås for deg: ", allergier[allergi])
    else:
        print("Denne allergien er ikke blitt registrert. Vi skal sørge for å oppdatere listen i løpet av dagen!")

allergi()
