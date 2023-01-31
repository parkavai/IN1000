# Oppgave 1.)

""" Lager en variabel "maanedfil" som inneholder info om maks temperatur per måned.
Deretter lager en funksjon som skal lage en ordbok ut av denne variabelen.
For å gjøre det benytter vi oss av en for-løkke som lager lister ut av innholdet
i "maanedfil". Deretter lager vi ordboken gjennom variablene som inneholder info
om temperatur eller hvilken måned det er. Tilslutt returneres ordboken og skriver
ut den.
"""
maanedfil = open("max_temperatures_per_month.csv")

ordbokmaaned = {}

def maaned(filnavn):
    for i in maanedfil:
        bitermaaned = i.split(",")
        maaned = bitermaaned[0]
        temperatur = bitermaaned[1]
        ordbokmaaned[maaned] = float(temperatur)
    return(ordbokmaaned)

maanedbok = maaned(maanedfil)

print(maanedbok)

# Oppgave 2.) og 3.)

""" Gjør samme fremgangsmåte som forrige bare at vi har en if-sjekk.
Nå skal vi ha en if-sjekk hvor den høyeste daglige temperaturen i en måned skal
erstatte den høyeste månedlige temperaturen for den måneden. For å gjøre dette så
må vi hente ordbokmaaned fra forrige deloppgave og bruke indeks 0. Indeksen sørger
for at vi slipper å gjøre programmet komplisert i forbindelse med hvordan vi skal
sammenligne en gitt temperatur for en måned og ikke alle månedene. Det gjør oppgaven enklere å
håndtere da vi allerede har en ordbok for hver måned. Skulle høyeste månedstemperaturen
i en gitt måned være mindre enn dagstemperaturen, skal dagstemperaturen erstatte
den høyeste månedlige temperaturen. For denne oppgaven er det Mai og Juli.
"""

dagligfil = open("max_daily_temperature_2018.csv")

def oppdaterordbokmaaned(maanedbok,daglig_temperatur):
    for t in daglig_temperatur:
        biterdaglig = t.split(",")
        maaned = biterdaglig[0]
        dag = int(biterdaglig[1])
        temperatur = float(biterdaglig[2])
        if ordbokmaaned[maaned] < temperatur:
            ordbokmaaned[maaned] = temperatur
            print("Ny varmerekord på ",maaned,  ":", temperatur, "grader. Den gamlevarmerekorden var på:", ordbokmaaned[maaned], "grader.")
    return ordbokmaaned

print(oppdaterordbokmaaned(ordbokmaaned,dagligfil))

# Oppgave 5.)

""" Ved å bruke en for-løkke som går gjennom innholdet i ordboken, er det mulig
å legge til alle verdiene i en ny fil med det samme formatet som max_temperatures_per_month.
Det er viktig at man lager filen som en global variabel slik at alle månedene og
deres temperatur, blir lagt til. """

oppdatertfil = open("oppdater.csv", "w")
def skrivutordbok(oppdatertmaanedbok,fil):
    for i in ordbokmaaned:
        format = f"{i},{ordbokmaaned[i]}\n"
        oppdatertfil.write(format)
    oppdatertfil.close()

skrivutordbok(ordbokmaaned,oppdatertfil)
