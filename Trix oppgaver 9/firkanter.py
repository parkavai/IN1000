class Side:
    def __init__(self, lengde, farge):
        self._lengde = lengde
        self._farge = farge

    def hentFarge(self):
        return self._farge

    def hentLengde(self):
        return self._lengde

    def printSide(self):
        print(self._lengde, self._farge)


class Firkant:
    def __init__(self):
        self._venstre = None
        self._hoyre = None
        self._topp = None
        self._bunn = None

    def leggTilSide(self, side, plassering):
        if plassering == "venstre":
            if self._venstre == None:
                self._venstre = side
                return True
            else:
                return False
        if plassering == "hoyre":
            if self._hoyre == None:
                self._hoyre = side
                return True
            else:
                return False
        if plassering == "topp":
            if self._topp == None:
                self._topp = side
                return True
            else:
                return False
        if plassering == "bunn":
            if self._bunn == None:
                self._bunn = side
                return True
            else:
                return False

    def fjernSide(self,side):
        if side == self._venstre:
            self._venstre = None
        if side == self._hoyre:
            self._hoyre = None
        if side == self._topp:
            self._topp = None
        if side == self._bunn:
            self._bunn = None

    def erFirkant(self):
        return self._venstre is not None and self._hoyre is not None and self._bunn is not None and self._topp is not None

bunn = Side(24,"blaa")
topp = Side(24,"blaa")
venstre = Side(24,"blaa")
hoyre = Side(24,"blaa")

firkanten = Firkant()
print(firkanten.erFirkant())
firkanten.leggTilSide(bunn,"bunn")
print(firkanten.erFirkant())
firkanten.leggTilSide(topp, "topp")
firkanten.leggTilSide(venstre, "venstre")
firkanten.leggTilSide(hoyre, "hoyre")
print(firkanten.erFirkant())
