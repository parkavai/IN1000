class Brev:
    def __init__(self, avsender,mottaker):
        self._avsender = avsender
        self._mottaker =  mottaker
        self._liste = []

    def skrivLinje(self,tekststreng):
        self._liste.append(tekststreng)

    def lesBrev(self):
        print("Hei,", self._mottaker)
        print()
        for linje in self._linjer:
            print(linje)
        print()
        print("Hilsen fra,")
        print(self._avsender)
