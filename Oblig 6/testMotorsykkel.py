from motorsykkel import Motorsykkel

""" Lager en prosedyre som skal lage 3 objekter hvor hver objekt består av
en motosykkel. Tilslutt addere den siste motorsykkelen sin km med 10 for å
sjekke om det fungerte. """

def hovedprogram():
    motorsykkel1 = Motorsykkel("HONDA", "1101", 15)
    motorsykkel2 = Motorsykkel("BMW", "2102", 40)
    motorsykkel3 = Motorsykkel("Harley-Davidson", "5212", 60)

    print(motorsykkel1.skrivUt())
    print(motorsykkel2.skrivUt())
    print(motorsykkel3.skrivUt())

    motorsykkel3.kjor(10)
    print(motorsykkel3.getKilometerstand())

hovedprogram()
