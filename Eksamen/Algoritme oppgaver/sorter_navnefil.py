def sorterNavnFil(filnavn):
    fil = open(filnavn, "r")
    personer = []
    hunder = []
    for linje in fil:
        data = linje.strip().split(" ")
        symbol = data[0]
        navn = data[1]
        if(symbol == "P"):
            personer.append(navn)
        else:
            hunder.append(navn)
    print("Oversikt over personer")
    for person in personer:
        print(person)
    print("")
    print("Oversikt over hunder")
    for hund in hunder:
        print(hund)

sorterNavnFil("navn.txt")