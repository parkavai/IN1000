
class Dag:

    def __init__(self, dato, nedbor):
        self._dato = dato
        self._nedbor = nedbor

    def __str__(self):
        return "Dato: " + self._dato + " - Nedbør: " + str(self._nedbor)

def lesinnfil(filnavn):
    fil = open(filnavn, "r")
    liste = []
    for linje in fil:
        skille = linje.strip().split('-')
        dato = skille[0]
        tallmm = skille[1].strip().split()
        tallkomma = tallmm[0].strip().split(",")
        tall = float(tallkomma[0]+tallkomma[1])
        tall = tall/10
        liste.append(Dag(dato,tall))
    return liste

def dagMax():
    liste = lesinnfil("Nedbørsmengder.txt")
    talliste = []
    heleliste = []
    for objekt in liste:
        nedborstall = objekt._nedbor
        talliste.append(nedborstall)
        heleliste.append(objekt)
    stoerste = talliste[0]
    for i in talliste:
        if i > stoerste:
            stoerste = i
    datoen = 0
    for dato in heleliste:
        if stoerste == dato._nedbor :
            datoen = dato._dato
    print("Datoen med størst nedbørsmengde er: ", datoen)

def tilsammen():
    liste = lesinnfil("Nedbørsmengder.txt")
    talliste = []
    for objekt in liste:
        nedborstall = objekt._nedbor
        talliste.append(nedborstall)
    sum = 0
    for i in talliste:
        sum +=i
    return sum

tilsammen()

# Alternativ

class Dag:

    def __init__(self, dato, nedbor):
        self.setDato(dato)
        self.setNedbor(nedbor)

    def setDato(self, dato):
        self._dato = dato

    def setNedbor(self, nedbor):
        self._nedbor = nedbor

    def __str__(self):
        return "Dato: " + self._dato + " - Nedbør: " + str(self._nedbor)

    def hentNedbor(self):
        return self._nedbor


def lesInnFil(filnavn):
    fil = open(filnavn, "r")
    dagListe = []
    for line in fil:
        # Lag ny Dag objekt
        elementer = line.split("-")
        # print(elementer[0].split())

        dato = elementer[0].strip()
        nedbor = elementer[1].strip()
        # Fjern 'mm'
        nedbor = nedbor[:-2].strip()

        # Erstatt ',' med '.'
        nedbor = nedbor.replace(',', '.')
        # Convert to float
        nedbor = float(nedbor)
        enDag = Dag(dato, nedbor)

        dagListe.append(enDag)
            # print(el.strip())

        # print(elementer)
    return dagListe


def dagMax(dagListe):
    topDag = None
    for dag in dagListe:
        if (topDag == None):
            topDag = dag
        elif(dag.hentNedbor() >= topDag.hentNedbor()):
            topDag = dag
    return topDag

def tilsammen(dagListe):
    totalMengde = 0
    for dag in dagListe:
        totalMengde += dag.hentNedbor()

    return totalMengde

def besteMaaned(dagListe):
    # Utfordring!
    pass

# Program
dagListe = lesInnFil("Nedbørsmengder.txt")
print(dagMax(dagListe))
print(tilsammen(dagListe))
