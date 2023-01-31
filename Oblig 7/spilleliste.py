from sang import Sang

# Oppretter klassen Spilleliste

class Spilleliste:

# Konstruktøren med instansvariablene self._sanger, self._navn, self.listesang

    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

        """ Åpner filen i en variabel kalt "sangene". Har en for-løkke som går igjennom
        hver enkelt linje i filen, hvor vi splitter sangen etter tegnet ";". Videre
        legger vi til artist og sangen som et objekt i listen som oppgaven ba om.
        Tilslutt lukker vi filen. """

    def lesFraFil(self,filnavn):
        sangene = open(filnavn)
        for sang in sangene:
            alleData = sang.strip().split(';')
            self._sanger.append(Sang(alleData[1],alleData[0]))
        sangene.close()

# Legger til et nytt sangobjekt i sanglisten

    def leggTilSang(self,nySang):
        self._sanger.append(nySang)

# Spiller en sang gjennom metoden i Sang-filen

    def spillSang(self, sang):
        sang.spill()

# Spiller alle sangene i listen

    def spillAlle(self):
        for spill in self._sanger:
            print(spill)

        """ Fjerner et sangobjekt i sanglisten. Dette gjøres gjennom if-betingelsen
        som sjekker om oppgitt sang er i sanglisten. Dermed fjerner sangen fra
        lista. """

    def fjernSang(self,sang):
        if sang in self._sanger:
            self._sanger.remove(sang)

        """ Finner oppgitt sang ved bruk av metoden fra Sang-filen. For-løkken går gjennom
        sang-listen hvor telleren går gjennom hvert element i sang-listen. Betingelsen ser om
        en oppgitt tittel finns i sang-listen hvor betingelsen sammenligner et element med
        oppgitt tittel. Oppfylles betingelsen returneres det elementet. """

    def finnSang(self,tittel):
        for gjennom in self._sanger:
            if gjennom.sjekkTittel(tittel):
                return gjennom;

        """ Ser om oppgitt artistnavn finns i sang-listen. For-løkken går gjennom
        sang-listen hvor telleren går gjennom hvert element i sang-listen. Betingelsen ser om
        en oppgitt artistnavn finns i sang-listen hvor betingelsen sammenligner artist-element med
        oppgitt artistnavn. Oppfylles betingelsen skal denne legges til i en ny liste med både
        artisten og han/hun sine titler. Tilslutt returneres listen. """

    def hentArtistUtvalg(self,artistnavn):
        self.listesang = [];
        for sjekk in self._sanger:
            if sjekk.sjekkArtist(artistnavn):
                self.listesang.append(sjekk);
        return self.listesang
