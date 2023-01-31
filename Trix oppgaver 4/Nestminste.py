liste = [1,1,3,2,6,4,5]

minste = liste[0]
for element in liste:
    if minste > element:
        minste = element
print(liste[minste+1])
