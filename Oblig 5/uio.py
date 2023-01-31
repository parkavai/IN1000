# Oppgave 1.)

uio = {}

# Oppgave 2.)

""" For å kunne utføre denne oppgaven, splitter man navnet til å konvertere
etternavnet om til en string. Deretter lage en variabel "bokstav" som inneholder
forbokstaven i et etternavn. Tislutt konkateneres fornavnet med bokstaven og
returnerer dette som brukernavn. """

def lagBrukernavn(navn):
    navn = navn.lower()
    biter = navn.split()
    fornavn = biter[0]
    etternavn = str(biter[1])
    for i in range(len(etternavn)):
        bokstav = etternavn[0]
        brukernavn = fornavn + bokstav
    return brukernavn

# Oppgave 3.)

suffix = "student.matnat.uio.no"

brukernavn = lagBrukernavn("Kari Nordmann")

def lagEpost(brukernavn,epostsuffix):
    epostadresse = brukernavn + "@" + epostsuffix
    return epostadresse

epost = lagEpost(brukernavn,suffix)

# Oppgave 4.)

""" Splitter epostadresse og lager en forløkke som sørger for å lage ordboken
vi vil opprette.  """

def printEposter(ordbok):
    biter = epost.split("@")
    for t in biter:
        ordbok[biter[0]] = biter[1]
    return ordbok

ordbokforepost = printEposter(uio)

# Oppgave 5.)

""" While-løkken vil fungere så lenge bruker ikke taster inn bokstaven s. I
tillegg må man sørge for at bruker kan ha muligheten til å avslutte programmet
selv etter å ha tastet inn bokstaven i eller p.  """

bruker = input("Skriv inn et av disse bokstavene: i eller p. Ved å taste inn s så avsluttes programmet.\n")

while bruker != "s":
    bruker = input("Vil du avslutte programmet? Tast inn s for å avslutte eller fortsett programmet med i eller p.\n")
    if bruker == "i":
        tastnavn = input("Skriv inn et navn med både fornavn og etternavn: ")
        brukernavn = lagBrukernavn(str(tastnavn))
        tastsuffiks = input("Skriv inn et suffiks: ")
        epost = lagEpost(brukernavn,tastsuffiks)
        ordbokforepost = printEposter(uio)
    elif bruker == "p":
        print(printEposter(ordbokforepost))
