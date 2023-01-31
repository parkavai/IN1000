# A
liste = ["en", "to", "tre"]

# B
teller = 0
while teller < len(liste) :
    print("Indeks", teller, ":", liste[teller])
    teller+=1

# C
fra_bruker = input("Gi en string:")
liste.append(fra_bruker)

print(liste)
