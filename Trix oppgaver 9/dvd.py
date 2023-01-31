class Dvd():
    def __init__(self, tittel, produsent, utgaveNummer):
        self._tittel = tittel
        self._produsent = produsent
        self._utgaveNummer = utgaveNummer


    def __str__(self):
        return self._tittel

    def __eq__(self, annenDvd):
        if(self._tittel == annenDvd._tittel):
            if(self._produsent == annenDvd._produsent):
                return self._utgaveNummer == annenDvd._utgaveNummer
        return False
