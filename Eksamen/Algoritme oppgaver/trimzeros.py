def trimZeros(liste):
    siste = len(liste) - 1
    forste = 0
    for x in range(len(liste) - 1):
        if(liste[siste] == 0):
            siste -= 1
        if(liste[forste] == 0):
            forste += 1
    return liste[forste:siste+1]

print(trimZeros([0,0,1,2,0,3,0,0,4,0]))
