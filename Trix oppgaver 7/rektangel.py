class Rektangel:
    def __init__(self, lengde, bredde):
        self._lengde = lengde
        self._bredde = bredde

    def oekLengde(self, oekning):
        self._lengde += oekning

    def oekBredde(self, oekning):
        self._bredde += oekning

    def areal(self):
        return (self._lengde * self._bredde)

    def omkrets(self):
        return (self._lengde * 2 + self._bredde * 2)

    #c) Utvid klassen med metoder for å redusere et objekt

    def reduserLengde(self,reduksjon):
        self._lengde -= reduksjon

    def reduserBredde(self, reduksjon):
        self._bredde -= reduksjon
    #Men disse er litt redundante, siden å redusere
    #er det samme som å øke med et negativt tall.

#oppretter to rektangler:
rektangel1 = Rektangel(5,10)
rektangel2 = Rektangel(6,9)

#Skriver ut begges areal
print(rektangel1.areal())
print(rektangel2.areal())

#Øker lengden på rektangel1 og bredden på rektangel2
rektangel1.oekLengde(5)
rektangel2.oekBredde(4)

#Skriver ut begges omkrets
print(rektangel1.omkrets())
print(rektangel2.omkrets())
