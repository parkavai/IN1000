listeEn = [[31], [14, 15, 16, 17, 18]]
listeTo = [[1,2,3], [2, 3, 4], [28, 31], [14, 15, 16, 17, 18]]
listeTre = [[1,2,3], [2, 3, 4], [28, 31], [14, 15, 16, 17, 18], [1, 2, 4, 5], [9, 12, 16, 19], [21, 23, 25, 27, 28]]

def maxBesok(liste):
    stoerste = len(liste[1])
    indeks = 0
    for i in range(0,len(liste)):
        indeks = len(liste[i])
        if indeks > stoerste:
            stoerste = indeks
            return stoerste
    return stoerste

def faerrestBesok(liste):
    minste = len(liste[0])
    indeks = 0
    for i in range(0,len(liste)):
        indeks = len(liste[i])
        if indeks < minste:
            minste = indeks
            return minste
    return minste

def alleBesok(liste):
    antallbesok = 0
    for i in range(0,len(liste)):
        antallbesok+=len(liste[i])
    return antallbesok

def hvemVarPaadato(liste,dato):
    for i in range(0,len(liste)):
        if dato in liste[i]:
            return liste[i]

print("Flest besok: " + str(maxBesok(listeEn)))
print("Flest besok: " + str(maxBesok(listeTo)))
print("Flest besok: " + str(maxBesok(listeTre)))

print("Faerrest besok: " + str(faerrestBesok(listeEn)))
print("Faerrest besok: " + str(faerrestBesok(listeTo)))
print("Faerrest besok: " + str(faerrestBesok(listeTre)))

print("Totalt antall besok: " + str(alleBesok(listeEn)))
print("Totalt antall besok: " + str(alleBesok(listeTo)))
print("Totalt antall besok: " + str(alleBesok(listeTre)))

print("Pasienter som var på sykehuset 15.: " + str(hvemVarPaadato(listeEn, 15)))
print("Pasienter som var på sykehuset 3.: " + str(hvemVarPaadato(listeTo, 3)))
print("Pasienter som var på sykehuset 2.: " + str(hvemVarPaadato(listeTre, 2)))
