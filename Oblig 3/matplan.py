# Oppgave 1

""" Lager en liste over de ulike måltidene for hver beboer. Legger til alle
listene i ordboken hvor navnet er nøkkelverdi og innholdsverdi er måltidene. """

maaltid1 = ["brød", "egg", "pølser"]

maaltid2 = ["havregryn", "kjøttboller", "burger"]

maaltid3 = ["yoghurt", "kylling", "pizza"]


beboer = {"Arne": maaltid1, "Bjørn": maaltid2, "Lise": maaltid3}

""" Har kalt prosedyren for matplan og skal gi oversikt for navnene som er
registrert. Deretter skal bruker taste inn et navn for å få tilgang til innholdet
som ligger i navnet som ble skrevet. Tilslutt kjøres en if-sjekk for å se om
navnet ligger i ordboka, hvis ikke får bruker en beskjed om det.
"""

def matplan():
    print(beboer)
    inp = input("Skriv inn et navn: ")
    navn = inp
    if navn in beboer:
        print("Her er matplanen for ", navn, beboer[navn])
    else:
        print("Navnet til denne beboeren er ikke registrert. ")

matplan()

# Oppgave 3

# a.)

""" En set kan fungere bra her siden vi skal lagre brukernavn til studentene.
Skulle noen brukere skrive samme brukernavn så vil en set sørge for at det ikke
er mulig å ha identiske brukernavn i systemet. I tillegg til at det ikke er
nødvendig med noe ordning i rekkefølgen heller. En ordbok er ikke nødvendig her
da flere kan ha samme navn som skaper problemer i henhold til ens eget
brukernavn og gjør prosedyren komplisert.
"""

# b.)

""" En ordbok ville fungert bra her siden ved å gi brukernavn som nøkkelverdi,
kan poengene lagres som verdier i disse nøklene. Dermed, om man vil få frem
poengene til en bruker, taster man inn brukernavnet slik at det kommer frem.
"""

# c.)

""" Her kan både en liste og set brukes, men jeg ville valgt en liste.
En ordbok er ikke nødvendig her når vi kun skal vise vinnere av hvem som vant i
lotto. En liste vil få frem alle vinnerne uten å måtte ta hensyn til identitet
siden hele navnet blir skrevet. I tillegg til at man investerer mindre tid ved
å lage en liste. Grunnen til at jeg foretrekker en liste framfor set skyldes
av at navnet består av både fornavn og etternavn, som tilsammen utgjør et unikt
navn. Derfor trengs ikke en mengde for denne oppgaven.

"""

# d.)

""" I denne oppgaven ville jeg brukt en ordbok. Årsaken er at i ordboken ville
f.eks nøtter vært en nøkkelverdi med en oversikt over de ulike matvarene som
inneholder nøtter. Det blir oversiktlig og strukturert for et selskap som skall
ha oversikt over allergier og matvarene som trigger de allergiene.
"""
