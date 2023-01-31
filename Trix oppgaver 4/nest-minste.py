def finnNestMinst(liste):
    minste = liste[0]
    for element in liste:
        if minste > element:
            minste = element
    while(minste in liste):
        liste.remove(minste)
    minste = liste[0]
    for element in liste:
        if minste > element:
            minste = element
    return minste



""" Jeg må finne ut om hvordan jeg skal gjøre om nestminst telleren til tallet
2, deretter lager jeg en if hvor om nestminst > minst, så skal tallet nestminst
printes ut."""
