from spillebrett import Spillebrett

def main():

    # Variabler hvor bruker taster inn rader og kolonner for brettet.

    Rader = int(input("Skriv inn rader for brettet: "))
    Kolonner = int(input("Skriv inn kolonner for brettet: "))

    # Lager spillebrettet utifra variablene over.

    spillebrett = Spillebrett(Rader,Kolonner)

    # En variabel som skal sørge for å oppdatere spillebrettet for hver gang man taster inn enter.

    brukerinput = ""

    """ En while-løkke som kjøres så lenge bruker ikke skriver inn q.
    I tillegg til en betingelse under som sørger for at brettet oppdateres. """

    while brukerinput != "q":
        brukerinput = input("Press enter for å fortsette. Skriv inn q og trykk enter for å fortsette ")
        if brukerinput == "":
            spillebrett.oppdatering()
            spillebrett.tegnBrett()
            print("Generasjon: ", spillebrett._generasjonsnummer, "- Antall levende celler: ", spillebrett.finnAntallLevende())


main()
