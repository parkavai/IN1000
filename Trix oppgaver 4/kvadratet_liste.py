# A
liste = [1, 2, 3, 4, 5]

# B
teller = 0
while teller < len(liste) :
    liste[teller] = liste[teller] * liste[teller]
    teller+=1
print(liste)
