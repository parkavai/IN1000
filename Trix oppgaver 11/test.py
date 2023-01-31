liste = [1,2,-3,4,-5,6]
total = 0
i = 0
while liste[i]>0:
    total +=liste[i]
    i +=1
i = len(liste)-1
print(i)
while liste[i]>0:
    total +=liste[i]
    i -=1
print(total)
