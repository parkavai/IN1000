class Student:
    def __init__(self, navn, brukernavn, tlf):
        self._navn = navn
        self._brukernavn = brukernavn
        self._tlf = tlf
    
    def printInfo(self):
        linje = "Navn: " + str(self._navn) + "\n"
        linje += "Brukernavn: " + str(self._brukernavn) + "\n"
        linje += "Telefonnummer: " + str(self._tlf) + "\n"
        return linje
    
    def hentnavn(self):
        return self._navn