""" Lager en klasse Dato som skal bestå av metoder hvor en en metode returener året,
en metode som skal konvertere en dato til en tekststreng og en metode med en
if-sjekk som ser om en dagen i en dato er det samme som en bestemt dag i en dato."""

class Dato:
    def __init__(self,nyDag,nyMaaned, nyttAar):
        self._nyDag = int(nyDag)
        self._nyMaaned = int(nyMaaned)
        self._nyttAar = int(nyttAar)
        self._dato = ""

    def leseAvAar(self):
        return self._nyttAar

    def stringDato(self):
        self._dato = str(self._nyDag) + "." + str(self._nyMaaned) + "." + str(self._nyttAar)
        return self._dato

    def sjekkeDato(self,dag):
        if self._nyDag == dag:
            return True
        else:
            return False
