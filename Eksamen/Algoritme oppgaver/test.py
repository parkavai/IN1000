string = "sadasdas"

siste = string[-1]
print(siste)
nestsiste = string[-1-1]
print(nestsiste)


def erHus(liste):
    forste = liste[0]
    forstesum = 0
    i = 0
    andre = 0
    andresum = 0
    while i < len(liste):
        if liste[i] != forste:
            andre = liste[i]
            if andre == liste[i]:
                andresum+=1
        elif liste[i] == forste:
            forstesum+=1
        i+=1
    if (forstesum == 3 and andresum == 2) or (andresum == 3 and forstesum == 2):
        return True

    # annet alternativ

    forste = liste[0]
    for i in liste:
        if forste != i:
            andre = i
    sum1 = liste.count(forste)
    sum2 = liste.count(andre)
    if sum1 == 2 and sum2 == 3 or sum2 == 2 and sum1 == 3:
        return True
    return False



def arverekke(forfader, etterkommer, forstefodte):
    mellom = forstefodte[forfader]
    nyliste = []
    nyliste.append(forfader)
    nyliste.append(etterkommer)
    for nokkel in forstefodte:
        if mellom in nokkel:
            nyliste.append(mellom)
    if (forfader in nyliste) and (etterkommer in nyliste) and (mellom in nyliste):
        return nyliste
    else:
        return []

barn = {"Halfdan":"Harald", "Christian":"Hans", "Harald":"Eirik"}
print(arverekke("Halfdan", "Eirik", barn))


def sjekk(liste):
    sjekksum = 0
    for i in range(len(liste)-1):
        if liste[i] <= liste[i+1]:
            sjekksum +=1
    if sjekksum == len(liste)-1:
        return True
    else:
        return False

print(sjekk([1,2,3,4,5,6,7]))

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

def likesifre(list):
    indeks = list[0]
    samlet = list.count(indeks)
    if samlet == len(list):
        return True
    else:
        return False

print(likesifre([1,1,1,1,1]))


def omfoersteindeksertall():
    found = False
    position = 0
    string = "Hdkasfkasd2"
    while not found and position < len(string) :
        if string[position].isdigit() :
            found = True
        else :
            position = position + 1
    if found :
        print("First digit occurs at position", position)
    else :
        print("The string does not contain a digit.")

def fylltiltallene(tallene):
    lengden = len(tallene)
    while lengden != 10:
        tallene.append(0)
        lengden +=1
    return tallene

s = (fylltiltallene([1,2,3,4,5,6]))

def lesinnFil(filnavn):
    fil = open(filnavn, "r")
    en = fil.readline()
    for linje in en:
        data = linje.split(",")
        print(data)
    print(en)

lesinnFil("tall.txt")

def dobbelListe(liste):
    nyListe = []
    for i in liste:
        nyListe.append(i)
        nyListe.append(42)
    return nyListe
