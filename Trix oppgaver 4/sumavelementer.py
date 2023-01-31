listen = [6,5,3,4,7,1,2,3,2,1]


def sumavelementer(liste):
    returverdi = False
    for i in range(0, len(listen)-2):
        if (liste[i] + liste[i+1] == liste[i+2]):
            print(liste[i],liste[i+1],liste[i+2])
            returverdi = True
    return returverdi

print(sumavelementer(listen))
