from sang import Sang

# Oppretter klassen Spilleliste

class Spilleliste:

# Konstruktøren med instansvariablene self._sanger, self._navn, self.listesang

    def __init__(self, listenavn, filnavn):
        self._sanger = []
        self._navn = listenavn
        self.listesang = []
        sangene = open(filnavn)

""" Åpner filen i en variabel kalt "sangene". Har en for-løkke som går igjennom
hver enkelt linje i filen, hvor vi splitter sangen etter tegnet ";". Videre
legger vi til artist og sangen som et objekt i listen som oppgaven ba om.
Tilslutt lukker vi filen. """

    def lesFraFil(self,filnavn):
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

""" Fjerner en et sangobjekt i sanglisten. Dette gjøres gjennom pop hvor teller
"k" iterer gjennom alle indeksene i listen. Gjennom betingelsen så vil den fjerne
den indeksen hvor sangobjektet ligger. Siden det listen består av et sangobjekt
med både artist og tittel, så vil betingelsen oppfylles hvis oppgitt sang er den
samme som elemtets tittel. """

    def fjernSang(self,sang):
        for k in range(len(self._sanger)):
            if(self._sanger[k] == sang):
                self._sanger.pop(k)

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

def hovedprogram():

    allMusikk = Spilleliste('Hele musikkbiblioteket')
    allMusikk.lesFraFil('musikk.txt')

    print("Tester spillAlle: Spiller alle sanger i listen:")
    allMusikk.spillAlle()
    print()

    nySang = Sang("Jahn Teigen", "Mil etter mil")
    print("Spiller ny sang:")
    allMusikk.spillSang(nySang)
    print()

    allMusikk.leggTilSang(nySang)
    print("Spiller alle sanger i listen inkl ny sang:")
    allMusikk.spillAlle()
    

hovedprogram()
