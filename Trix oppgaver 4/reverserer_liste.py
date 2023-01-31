liste = [1, 2, 3, 4, 5, 6]

teller_opp = 0
teller_ned = len(liste)-1
halve_listen = len(liste)//2

while teller_opp < halve_listen :
    tmp = liste[teller_opp]
    liste[teller_opp] = liste[teller_ned]
    liste[teller_ned] = tmp

    teller_opp+=1
    teller_ned-=1

print("Ny liste:")
print(liste)
