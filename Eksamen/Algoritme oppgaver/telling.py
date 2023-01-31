def telling(streng):
    liste = []
    for bokstav in streng:
        if (bokstav not in liste):
            liste.append(bokstav)
    return len(liste)

print(telling("aaaabbbbcccddd"))

i = 0

def null_ut2(liste):
    ny_liste = []
    for i in liste:
        liste[i] = 0

terningkast = [1,2,3,3,5,6]

null_ut2(terningkast)
print(terningkast[2])