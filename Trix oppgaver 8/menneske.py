class Menneske():

    def __init__(self,Navn,Alder):
        self._Navn = Navn
        self._Alder = Alder
        self._erForelder = False
        self._barn = []

    def Fodselsdag(self):
        self._Alder = self._Alder + 1
        print("Gratulerer med til,", self._Navn, " med ", self._Alder, " dagen")

    def byttenavn(self,nyttNavn):
        self._Navn = nyttNavn

    def FaaBarn(self,navn):
        self._erForelder = True
        self._barn.append(Menneske(navn, 0))

    def hentBarn(self):
        return self._barn


def hovedprogram(arg):
    geir = Menneske("Geir", 45)
    print(geir._alder)
    geir.fodselsdag()
    print(geir._alder)
    geir.byttNavn("Kjell")
    geir.faaBarn("Geirine")
    barneListe = geir.hentBarn()
    for barn in barneListe:
        print(barn._navn)
