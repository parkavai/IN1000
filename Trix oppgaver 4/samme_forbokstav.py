personer = {}

inn = "y"
while inn == "y":
    navn = input("Oppgi navn: ")

    gyldigAlder = False

    while gyldigAlder != True:
        alder = input("Oppgi alder: ")
        if (alder.isdigit()):
            gyldigAlder = True
            personer[navn] = int(alder)
        else:
            print("Ugyldig input!")

    inn = input("Skriv \"y\" for aa taste inn flere navn: ")

bokstav = ""
while len(bokstav) != 1:
    bokstav = input("Oppgi en bokstav: ")
    if len(bokstav) != 1:
        print("Ugyldig input!")

bokstav = bokstav.lower()

for key in personer:
    if key[0].lower() == bokstav:
        print(key, personer[key])
