class Hytte:

    def __init__(self, navn, senger, pris):
        self._hyttenavn = navn
        self._senger = int(senger)
        self._pris = int(pris)

    def hentNavn(self):
        return self._hyttenavn

    def totPris(self,antPersoner):
        return self._pris*antPersoner

    def sjekkPlass(self,personer):
        if self._senger >= personer:
            return True
        else:
            return False

    def __str__(self):
        string = self._hyttenavn, self._senger, self._pris
        return string

    def __eq__(self,annen):
        if self.hentNavn() == annen.hentNavn():
            if self._senger == annen._senger:
                if self._pris == annen._pris:
                    return True
        return False

class Tur:

    def __init__(self,listeAvHytter, turBeskrivelse):
        self._listeAvHytter = listeAvHytter
        self._turBeskrivelse = turBeskrivelse

    def skrivTur(self):
        print(self._turBeskrivelse)
        print()
        print("Under er oversikt over alle hyttene: ")
        for hytte in self._listeAvHytter:
            print(hytte)

    def sjekkPrisPlass(self,personer,maksbeloep):
        for hytte in self._listeAvHytter:
            if (hytte.totPris(personer) < maksbeloep) and (hytte.sjekkPlass(personer)):
                return True
            return False

    def hentAntHytter(self):
        return len(self._listeAvHytter)

class TurPlanlegger:

    def __init__(self, hyttetext,turertext):
        self._hytteOrdbok = self._hytterFraFil("hytter.txt")
        self._turerListe = self._turerFraFil("turer.txt")

    def _hytterFraFil(self,filnavn):
        hyttefil = open(filnavn)
        hytteordbok = {}
        for hyttene in hyttefil:
            data = hyttene.strip().split()
            hyttenavn = str(data[0])
            antSenger = int(data[1])
            pris = float(data[2])
            hytteordbok[hyttenavn] = Hytte(hyttenavn,antSenger,pris)
        hyttefil.close()
        return hytteordbok


    def _turerFraFil(self,filnavn):
        turfil = open(filnavn)
        turer = []
        hytteliste = []
        beskrivelse = turfil.readline()
        hytter = turfil.readline()
        for linje in hytter:
            enhverhyttenavn = linje.strip().split()
            hytteliste.append(self._hytteOrdbok[enhverhyttenavn])
        turer.append(Tur(hytteliste,beskrivelse))
        turfil.close()
        return turer

            """
            tfil = open(filnavn,"r")
            turer = []
            linje = tfil.readline().strip()
            while linje != "":
                linje2 = tfil.readline()
                hyttenavn = linje2.split()
                hytteliste = []
                for ettNavn in hyttenavn:
                    hytteliste.append(self._hytteOrdbok[ettNavn])
                turer.append(Tur(hytteliste,linje))
                linje = tfil.readline().strip()
            tfil.close()
            return turer
            """

    def finnTurer(self, personer, maksbeloep, dager):
        for turer in self._turerListe:
            if (turer.sjekkPrisPlass(personer,maksbeloep)) and (turer.hentAntHytter() < dager):
                turer.skrivTur()

def hovedprogram() :
	turplaner = TurPlanlegger("hytter.txt", "turer.txt")
	turplaner.finnTurer(7, 7000, 5)

hovedprogram()
