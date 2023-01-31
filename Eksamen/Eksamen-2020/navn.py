"""
def beOmNavn(navneliste):
    brukerinput = str(input("Trykk enter "))
    navn = "erstatt"
    while(brukerinput != navn):
        brukerinput = str(input("Angi et navn: "))
        for x in navneliste:
            if(brukerinput == x):
                navn = x
    return navn
"""

def beOmNavn(navneliste):
    brukerinput = str(input("Angi et navn: "))
    if brukerinput in navneliste:
        return brukerinput + " finnes i lista"
    else:
        while(brukerinput not in navneliste):
            print("Feil navn, prøv igjen ")
            brukerinput = str(input("Angi et navn: "))
        return brukerinput + " finnes i lista"

print(beOmNavn(["parka", "rcsan", "kangey"]))