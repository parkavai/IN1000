def lengre_liste(liste):
    nyliste = []
    y = 1
    for x in range(len(liste)):
        nyliste.append(liste[x])
        if (y % 2 == 1):
            nyliste.append(42)
        y = 2*y + 1
    return nyliste

print(lengre_liste(["Suppe",8,"Krabbeklo"]))