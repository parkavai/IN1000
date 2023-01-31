""" Lager en klasse Motorsykkel som skal bestå av metoder hvor en en metode adderer
kilometerstanden med det gitte antall km, en metode returnerer den totale kilometerstanden,
og en metode som skriver ut alle instansvariablene for motosykkelen. """

class Motorsykkel:
    def __init__(self,merke,registreringsnummer,kilometerstand):
        self._merke = merke
        self._registreringsnummer = registreringsnummer
        self._kilometerstand = kilometerstand
        self._totale_kilometerstand = 0

    def kjor(self,km):
        self._totale_kilometerstand = self._kilometerstand + km

    def getKilometerstand(self):
        return self._totale_kilometerstand

    def skrivUt(self):
        motorsykkel = self._merke + " " + self._registreringsnummer + " " + str(self._kilometerstand)
        return motorsykkel
