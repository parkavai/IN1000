""" Lager en prosedyr som heter billett. Omgjør tallet som bruker taster inn
som alder, til et heltall. Deretter kjører if-setningene som hver printer ut en
melding basert på alder som ble tastet inn. I tillegg oppdateres prisen etter
hvilken betingelsen som blir oppfylt. Konvertere tallene om til string for å få
skrevet ut de diverse meldingene.
"""

def billett():
    inp = input("Skriv inn en alder: ")
    alder = int(inp)
    billettpris = 0
    if alder <= 17:
        billettpris = 30
        print("For deg som er " + str(alder) + " år, skal du kjøpe en barnebillett som vil koste: " + str(billettpris) + " kr.")
    elif alder > 17 and alder < 63:
        billettpris = 50
        print("For deg som er " + str(alder) + " år, skal du kjøpe en voksenbillett som vil koste: " + str(billettpris) + " kr.")
    else:
        billettpris = 35
        print("For deg som er " + str(alder) + " år, skal du kjøpe en pensjonsbillett som vil koste: " + str(billettpris) + " kr.")

billett()

billett()

billett()

# Problemer med prosedyren

""" Problemer som kan oppstå er hvis brukeren skriver en alder som ikke er
fornuftig for denne prosedyren. Et eksempel er 130 eller 0 som tilsvarer
slike verdier. Likevel vil de få en melding på dette med billetten som gjelder
for den aldersgruppen. Derfor kunne det vært nødvendig med en grense på hvor
alderen går. Eller at man ikke har tatt hensyn til ungdomsbillett, rabatt for
studenter eller rabatt generelt i systemet.
 """
