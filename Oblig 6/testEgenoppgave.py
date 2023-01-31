from egenoppgave import Person

""" Jeg valgte å gå med en betingelse hvor brukeren kan avslutte programmet
skulle han taste inn "nei". Ellers kan bruker legge til hobbyene hans inntill
betingelsen ikke er oppfylt. """

def hovedprogram():
    brukernavn = input("Skriv inn navn: ")
    brukeralder = input("Skriv inn alder: ")
    brukerhobby = input("Trykk på nei hvis du ikke vil fortsette å legge til hobbyer. ")

    person1 = Person()

    while brukerhobby != "nei":
        brukerhobby = input("Skriv inn hobby eller tast inn nei for å slutte: ")
        person1.leggTilHobby(brukerhobby)
    print(person1.skrivUt(brukernavn,brukeralder))

hovedprogram()
