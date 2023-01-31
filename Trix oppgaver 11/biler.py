class Person:
    def __init__(self, navn):
        self._mineBiler = [] # Biler personen eier
        self._laanteBiler = [] # Biler som personen laaner, men noen andre eier
        self._navn = navn

    def laanebil(self,indeks):
        self._laanteBiler.append(self._mineBiler[indeks])
        self._mineBiler.pop(indeks)

class Bil:
    def __init__(self, farge, merke):
        self._farge = farge
        self._merke = merke
        self._eier = None

    def Setteier(self,eier):
        self._eier = eier
        eier._mineBiler.append(bil)
