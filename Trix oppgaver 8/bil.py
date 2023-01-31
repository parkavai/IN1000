class Bil:
    def __init__(self, eier) :
        self._eier = eier

    def skriv_ut(self) :
        print(self._eier)

bil1 = Bil("Magne")
bil2 = Bil("Kjell")
bil2.skriv_ut()
