

# Oppretter klassen Sang
class Sang:

# Konstruktøren med instansvariablene tittel og artist

    def __init__(self,artist,tittel):
        self._tittel = tittel
        self._artist = artist

        """ En metode som skriver ut sangobjektet til en string. """

    def __str__(self):
        return "Spiller " + self._tittel + " av " + self._artist

        """ En metode som skriver ut sangobjektet gjennom metoden over. """

    def spill(self):
        print(self.__str__())

        """ Ser om oppgitt tittel er den samme som sangobjektets tittel. Bruker lower
        for å kunne konvertere bokstavene til små bokstaver. """

    def sjekkTittel(self,tittel):
        if tittel.lower() == self._tittel.lower():
            return True
        else:
            return False

        """ Ser om oppgitt artistnavn er det samme som objektets navn. Uavhengig om
        det tastes inn et eller flere navn. Split er essensielt for å kunne utføre denne
        testen da artistnavnet splittes om til elementer i en liste. Gjennom for-løkken
        blir telleren konvertert til de elementene i lista. If-betingelsen ser om en del av
        artistnavnet er det samme som navnet som er tastet inn. Hvis betingelsen oppfylles,
        vil den returnere true."""

    def sjekkArtist(self,navn):
        navn = str(navn.lower())
        self._artist = self._artist.lower()
        for i in self._artist.split():
            if i in navn:
                return True

        """ Ser om oppgitt artist og tittel er det samme som sangobjektets instansvariabler.
        Igjen benytter lower for å kunne konvertere bokstavene som er skrevet inn som
        små bokstaver for å kunne utføre betingelsen. """

    def sjekkArtistOgTittel(self,artist,tittel):
        if self.sjekkTittel(tittel.lower()) and self.sjekkArtist(artist.lower()):
            return True
        else:
            return False
