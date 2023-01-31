""" For å kunne skrive ut pasienten som har flest besøk, gjør vi følgende:
Vi har en variabel kalt flestBesok og en variabel kalt listenr. Hensikten med
variabel flestBesok, er å bruke denne variabelen for å sammenligne telleren i
for-løkken. Gjennom if-betingelsen, så sier den at: teller "i" går gjennom hele
listen. Hvis listen er større enn variabel flestbesok, så vil flestbesok bli
endret til lengden av en pasient som har flere besøk enn de andre. Deretter vil
"listenr" bli oppdatert til den pasienten med flest nummere. """

def maxBesok(liste):
    flestBesok = len(liste[0])
    listenr = 0
    for i in range(len(liste)):
        if len(liste[i]) > flestBesok:
            flestBesok = len(liste[i])
            listenr = i

    return listenr + 1 # siden listen på index 0 er pasient 1 sin liste.

def faerrestBesok(liste):
    minstBesok = len(liste[0])
    listenr = 0
    for i in range(len(liste)):
        if len(liste[i]) < minstBesok:
            minstBesok = len(liste[i])
            listenr = i

    return listenr + 1

def alleBesok(liste):
    totalBesok = 0
    for li in liste:
        totalBesok += len(li)
    return totalBesok


def hvemVarPaadato(liste, dato):
    pasientListe = []
    if dato < 1 or dato > 31: # ugyldig dato
        return False

    for i in range(len(liste)): #for hver indre liste
        for elem in liste[i]: #for hvert element i indre liste
            if elem == dato:
                pasientListe.append(i+1)

    return pasientListe

listeEn = [[31], [14, 15, 16, 17, 18]]
listeTo = [[1,2,3], [2, 3, 4], [28, 31], [14, 15, 16, 17, 18]]
listeTre = [[1,2,3], [2, 3, 4], [28, 31], [14, 15, 16, 17, 18], [1, 2, 4, 5], [9, 12, 16, 19], [21, 23, 25, 27, 28]]

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
