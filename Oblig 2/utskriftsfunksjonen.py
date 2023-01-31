# Oppgave 1.)

""" Lager en funksjon for lagring av navn og bosted. Har valgt å kalle
den for person som lagrer variablene navn og bosted. Verdiene tastes inn gjennom
input funksjonen. """

def person():

    navn = input("Skriv inn navn: ")

    bosted = input("Hvor kommer du fra? ")

# Tilslutt skrives ut meldingen som oppgaven foreslo at vi skulle gjøre.

    print("Hei, " + navn + "! " + "Du er fra " + bosted + "." + "\n")

# Oppgave 2.) For å kunne lagre info om 3 personer, behøver en kun å skrive ut
# funksjon gjentatte ganger som vist under.

person()
person()
person()
