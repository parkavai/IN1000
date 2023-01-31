class RaskBil:
    def __init__(self, merke, bilnummer,navn,motortype,maksHastighet):
        self._merke = merke
        self._bilnummer = bilnummer
        self._navn = navn
        self._motortype = motortype
        self._maksHastighet = int(maksHastighet)


    def skrivInfo(self):
        return self._merke, self._bilnummer, self._navn, self._motortype,
        self._maksHastighet

    def hentMotor(self):
        return self._motortype


bil1 = RaskBil("BMW", "1120", "Eddy", "Diesel", 45)

bil2 = RaskBil("Toyota", "1020", "Jimmy", "El", 65)

bil3 = RaskBil("Hondaru", "2020", "Sambeh", "Bensin", 35)

liste = [bil1,bil2,bil3]

for skriv in liste:
    if skriv.hentMotor() == "El":
        skriv.skrivInfo()
        print(skriv.skrivInfo())
