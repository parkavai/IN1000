class EspressoMaskin:
    def __init__(self, makskapasitet):
        self._MAKS = makskapasitet
        self._vannmengde = 1000

    def lagEspresso(self):
        if self._vannmengde >= 40:
            self._vannmengde -= 40
            print("Vær så god, en espresso.")
        else:
            print("Det er ikke nok vann til en espresso.")

    def lagLungo(self):
        if self._vannmengde >= 110:
            self._vannmengde -= 110
            print("Vær så god, en lungo.")
        else:
            print("Det er ikke nok vann til en lungo.")

    def fyllVann(self, ml):
        if ml <= self._MAKS - self._vannmengde:
            self._vannmengde += ml
            print("Fylte på med",ml,"ml vann.")
            print("Det er nå",self._vannmengde,"ml igjen.")
        else:
            print("Det er ikke plass til så mye vann.")

    def hentVannmengde(self):
        return self._vannmengde
