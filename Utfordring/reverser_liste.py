def reverser(liste):
    peker = len(liste) - 1
    nyListe = []
    while peker >= 0:
        nyListe.append(liste[peker])
        peker -= 1
    return nyListe

print(reverser(["en", "pluss", "to", "pluss", "tre", "er", "seks"]))