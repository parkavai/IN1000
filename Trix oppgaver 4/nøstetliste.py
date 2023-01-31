oliste = []

for o in range(0,5):
    oliste.append("o")



stjerneliste = []

for stjerne in range(0,5):
    stjerneliste.append("*")

rutenett = []

rutenett.append(oliste)

rutenett.append(stjerneliste)

rutenett.append(oliste)

for teller in rutenett:
    print(teller)
