# Oppgave 1.)

""" Lager en liste utifra hva den skal inneholde. Bruker range
som går fra 0-5 hvor bruker taster inn steder innenfor den grensen.
"""

steder = []

for stedsteller in range(0,5):
    inp = input("Skriv inn 5 ulike steder: ")
    taste = inp
    steder.append(taste)


# Oppgave 2.)

# Bruker samme fremgangsmåte, men ersatter navnet på lista.

klesplagg = []

print("")
for klesplaggteller in range(0,5):
    inp = input("Skriv inn 5 ulike klesplagg: ")
    taste = inp
    klesplagg.append(taste)

avreisedatoer =[]

print("")
for avreisedatoteller in range(0,5):
    inp = input("Skriv inn 5 ulike avreisedatoer: ")
    taste = inp
    avreisedatoer.append(taste)


# Oppgave 3.)

# Lager en ny liste som består av de tre listene ovenfor.

reiseplan = [steder, klesplagg, avreisedatoer]


# Oppgave 4.)

# Skriver ut alle listene.

print("")
for reiseplanteller in reiseplan:
    print(reiseplanteller)


# Oppgave 5.)

""" Lager to variabler som står for hver indeks. Bruker en if-betingelse som
ser om variabel "i1" er gyldig eller ikke. Deretter går vi inn i en ny
if-betingelse som ser om variabel "i2" er gyldig eller ikke. Hvis betingelsene
oppfylles, skal bruker få oversikt over hvilken liste som ble tatt ut og
hvilken verdi som ble skrevet ut av den listen. """

inp1 = input("Skriv inn et gyldig tall mellom 0 og 2 for indeks 1: ")
i1 = int(inp1)

inp2 = input("Skriv inn et gyldig tall mellom 0 og 4 for indeks 2: ")
i2 = int(inp2)

if i1 >= 0 and i1 <= 2:
    if i2 >= 0 and i2 <= 4:
        print(reiseplan[i1][i2])
    else:
        print("Ugyldige plasseringer")
else:
    print("Ugyldige plasseringer")
