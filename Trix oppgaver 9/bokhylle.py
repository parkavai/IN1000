class Bok:

    def __init__(self, tittel, utgivelsesaar, forfatter):
        self._tittel = tittel
        self._utgivelsesaar = int(utgivelsesaar)
        self._forfatter = forfatter

    def hentNavn(self):
        return self._tittel

    def hentUtgivelsesaar(self):
        return self._utgivelsesaar

    def printBok(self):
        print(self._tittel + " - " + self._forfatter + " - " +  str(self._utgivelsesaar))

class Bokhylle:

    def __init__(self, maksplass):
        self._maksplass = int(maksplass)
        self._boker = []

    def erDetPlass(self):
        if len(self._boker) != self._maksplass:
            return True
        else:
            return False

    def leggTilBok(self,bok):
        if self.erDetPlass() == True:
            self._boker.append(bok)
            return True
        else:
            return False

    def finnBok(self,navn,utgivelsesaar):
        for i in self._boker:
            if navn == i.hentNavn() and utgivelsesaar == i.hentUtgivelsesaar():
                return True
        return False

    def printBokhylle(self):
        for bok in self._boker:
            bok.printBok()

def hovedprogram():
    bok1 = Bok("hei", 2001, "rambo")
    hylle = Bokhylle(5)
    hylle.leggTilBok(bok1)
    hylle.printBokhylle()

hovedprogram()
