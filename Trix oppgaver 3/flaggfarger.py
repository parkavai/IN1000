flaggOrdbok = {"norge" : ["rødt", "hvitt", "blått"],
"sverige" : ["blått", "gult"],
"danmark" : ["rødt", "hvitt"],
"finland" : ["hvitt", "blått"],
"japan" : ["rødt", "hvitt"],
"gabon" : ["grønt", "gult", "blått"],
"storbritannia" : ["rødt", "blått", "hvitt"],
"chile" : ["blått", "hvitt", "rødt"]
}

flaggOrdbok["frankrike"] = "blått", "hvitt", "rødt"

def land():
    inp = input("Skriv inn et land: ")
    land = inp
    print(flaggOrdbok[land])

land()

"""

# Oppgave 2
flaggOrdbok["usa"] = ["blått", "rødt", "hvitt"]


# Oppgave 3
def flaggFargeProsedyre():
    land = input("Skriv inn navnet til et land: ")
    land = land.lower() # .lower() gjør om til små bokstaver.

    if land in flaggOrdbok:
        print(flaggOrdbok[land])
    else:
        print("Landet", land, "er ikke registrert i ordboken.")

flaggFargeProsedyre()

"""
