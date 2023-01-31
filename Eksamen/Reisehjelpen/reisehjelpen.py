class Attraksjon:
    def __init__(self, navn, barn, fra, til):
        self._navn = navn
        self._barn = barn
        self._fra = int(fra)
        self._til = int(til)

    def skrivAttr(self):
        utskrift = self._navn + ". " + str(self._fra) + " - " + str(self._til)
        if self._barn:
            utskrift = "BARN: " + utskrift
        else:
            utskrift = "VOKSEN: " + utskrift
        print(utskrift)

    def forBarn(self):
        return self._barn

    def aapenIPeriode(self,fra,til):
        if fra > self._til or til < self._fra:
            return False
        return True

class Destinasjon:
    def __init__(self, navn, arraylist):
        self._navn = navn
        self._arraylist = arraylist

    def hentDestNavn(self):
        return self._navn

    def skrivDest(self):
        print("Destinasjon:", self._navn)
        for attraksjoner in self._arraylist:
            attraksjoner.skrivAttr()

    def leggTilAttr(self,nyAttr):
        self._arraylist.append(nyAttr)

    def antallAktuelleAttr(self,barn,fraDato,tilDato):
        total = 0
        for individer in arraylist:
            if (individer.forBarn() or not barn) and individer.aapenIPeriode(int(fraDato),int(tilDato)):
                total += 1
        return total

class Katalog:
    def __init__(self):
        self._destKatalog = {}

    def skrivDestListe(self):
        for destinasjoner in self._destKatalog:
            print(destinasjoner)

    def skrivEnDest(self,destNavn):
        if destNavn in self._destKatalog:
            self._destKatalog[destNavn].skrivDest()
        else:
            print("Ingen destinasjoner med navnet: ", destNavn)

    def nyAttr(self,destNavn,attrNavn,barneVennlig,apenFra,apenTil):
        if destNavn in self._destKatalog:
            nyAttr = Attraksjon(attrNavn, barneVennlig, apenFra, apenTil)
        self._destKatalog[destNavn].leggTilAttr(nyAttr)

    def nyDestFraFil(self,destNavn,filnavn):
        if destNavn not in self._destKatalog:
            self._destKatalog[destNavn] = Destinasjon(destNavn, [])

        fil = open(filnavn, "r")
        attrNavn = fil.readline().rstrip()
        while attrNavn != "":
            hvem = fil.readline().rstrip()
            if hvem == "VOKSNE":
                forBarn = False
            else:
                forBarn = True
            fraDato = int(fil.readline().rstrip())
            tilDato = int(fil.readline().rstrip())
            self.nyAttr(destNavn, attrNavn, forBarn, fraDato, tilDato)
            attrNavn = fil.readline().rstrip()

    def finnBesteDest(self, barn, fra, til):
        besteDest = ""
        besteAntall = 0
        for destNavn in self._destKatalog:
            dest = self._destKatalog[destNavn]
            antall = dest.antallAktuelleAttr(barn, fra, til)
            if antall > besteAntall:
                besteDest = destNavn
                besteAntall = antall
        return besteDest


def hovedprogram():
    katalog = Katalog()
    katalog.nyDestFraFil("Slottet","abel.txt")
    katalog.skrivEnDest("Slottet")

hovedprogram()
