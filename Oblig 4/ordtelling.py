# Oppgave 1.)

""" For å vise hvor mange bokstaver det er i ordet, brukes funksjonen "len"
som viser lengden til en gitt verdi. """

def antallbokstaver(ord):
    return(len(ord))

# Oppgave 2.)

""" Gjennom bruken av split, lages det lister for hvert ord som ligger i stringen
som bruker har tastet inn. I funksjonen "Ordbok", lages en for løkke hvor teller
i går igjennom listen "ordene". For å legge til antall ganger et ord blir vist
i ordboken, brukes funksjonen "count" som teller antall ganger det ordet blir
nevnt i tekststrengen. Tilslutt printes ut meldingen utifra hvordan oppgaven
ville at meldingen skulle printes. """

inp = input("Skriv inn en setning: \n")

tekst = inp

antall = 0

ordene = tekst.split()

ordbokfortekst = {}

def ordbok():
    for i in ordene:
        ordbokfortekst[i] = ordene.count(i)
        print("Ordet ",  i, " forekommer", ordbokfortekst[i], "ganger, og har ", antallbokstaver(i), " bokstaver" )

# Oppgave 3.)

# Utførelse av programmet

print("Det er " + str(len(ordene)) + " ord i setningen din.")

ordbok()
