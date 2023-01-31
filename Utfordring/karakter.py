# Oppgave 1

def sorter_etter_karakter(filnavn):
    fil = open(filnavn,"r")
    ordbok = {}
    for linje in fil:
        data = linje.strip().split(",")
        navn = data[0]
        karakter = data[1]
        if karakter not in ordbok:
            ordbok[karakter] = []
        ordbok[karakter].append(navn)
    return ordbok 

# print(sorter_etter_karakter("karakter.csv"))

karakterOrdbok = sorter_etter_karakter("karakter.csv")

# Oppgave 2
def skriv_ut_sortert(ordbok):
    sortertKarakterOrdbok = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": []
    }
    for nokkel in ordbok.keys():
        sortertKarakterOrdbok[nokkel] = ordbok[nokkel]
    return sortertKarakterOrdbok

# print(skriv_ut_sortert(karakterOrdbok))

# Oppgave 3

def hent_vanligste_karakter(karakterOrdbok):
    vanligste_karakter = ""
    flest = 0
    for nokkel in karakterOrdbok:
        lengde = len(karakterOrdbok[nokkel])
        if(lengde > flest):
            flest = lengde 
            vanligste_karakter = nokkel
    return vanligste_karakter

print(hent_vanligste_karakter(karakterOrdbok))    