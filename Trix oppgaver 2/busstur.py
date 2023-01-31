passasjer = 30

inp1 = input("Stasjon1: Hvor mange gaar paa bussen: \n")
stasjon1 = int(inp1)
if stasjon1 >= passasjer:
    print("Bussen er full. ", (stasjon1-passasjer), " må gå til fots")
else:
    print("Det er plass til flere passasjerer: ", (30-stasjon1), " stykker" )

passasjer1 = passasjer - stasjon1



inp2 = input("Stasjon2: Hvor mange gaar paa bussen: \n")
stasjon2 = int(inp2)
if stasjon2 >= passasjer1:
    print("Bussen er full. ", (stasjon2-passasjer1), " må gå til fots")
else:
    print("Det er plass til flere passasjerer: ", (30-passasjer1), " stykker" )

passasjer2 = passasjer1 - stasjon2


inp3 = input("Stasjon3: Hvor mange gaar paa bussen: \n")
stasjon3 = int(inp3)
if stasjon3 >= passasjer2:
    print("Bussen er full. ", (stasjon3-passasjer2), " må gå til fots")
else:
    print("Det er plass til flere passasjerer: ", (30-passasjer2), " stykker" )
