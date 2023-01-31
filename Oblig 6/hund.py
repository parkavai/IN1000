""" Lager en klasse Hund som skal bestå av metoder med if-sjekk som returnerer
en vekt utifra mettheten og hvilke metode vi skal benytte. """

class Hund:
    def __init__(self,alder,vekt):
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10

    def spring(self):
        self._metthet = self._metthet - 1
        if self._metthet < 5:
            self._vekt = self._vekt - 1
            return self._vekt

    def spis(self,heltall):
        self._metthet = self._metthet + heltall
        if self._metthet > 7:
            self._vekt = self._vekt + 1
            return self._vekt

    def getAlderVekt(self):
        return self._alder, self._vekt
