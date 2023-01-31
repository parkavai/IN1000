class Gave:

    def __init__(self, navn, pris):
        self._gaveNavn = navn
        self._prisGave = pris

    def hentGavePris(self):
        return self._prisGave

    def hentGaveNavn(self):
        return self._gaveNavn

    def __str__(self):
        string = self._gaveNavn, self._prisGave
        return string

class Barn:

    def __init__(self, navnTilBarn):
        self._navnTilBarn = navnTilBarn
        self._listeMedGaver = []
        self._totalSum = 0

    def hentNavnTilBarn(self):
        return self._navnTilBarn

    def apneGave(self,gave):
        self._listeMedGaver.append(gave)
        self._totalSum += gave.hentGavePris()

    def hentTotalSum(self):
        return self._totalSum

    def skrivBarn(self):
        print("Her er de åpnede gavene til: ", self._navnTilBarn)
        for gavene in self._listeMedGaver:
            print(gavene)
        print("Totalsummen er: ", self._totalSum)

class Julekalender:

    def __init__(self, barneNavn,gavefilen ):
        self._apnere = []
        self._kalender = []
        for navn in barneNavn:
            self._apnere.append(Barn(navn))
        self._nesteApner = 0
        self._dag = 0
        self._lesGavefil(gavefilen)
        self._historikk = {}

    def nyDag(self):
        if self._dag > 23:
            str = "Alle gavene er åpnet"
            return str

        apner = self._apnere[self._nesteApner]
        apner.apenGave(self._kalender[self._dag])
        self._dag +=1
        self._nesteApner +=1

        if self._nesteApner >= len(self._apnere):
            self._nesteApner = 0

    def gaveOversikt(self):
        for barn in self._listeAvBarn:
            barn.skrivBarn()

    def _lesGavefil(self,gavefilen):
        fil = open(gavefilen,"r")
        for data in fil.strip().split(","):
            gaveNavn = data[0]
            gavePris = float(data[1])
            self._kalender.append(Gave(gaveNavn,gavePris))

    def _lesHistorikk(self,histFilNavn):
        fil = open(historikkFil,"r")
        for data in fil.strip().split(","):
            barneNavn = data[0]
            self._historikk[barneNavn] = []
            for gavenavn in data[1:]:
                self._historikk[barneNavn].append(gavenavn)

    def avvergetLike(self):
        gaveFraDag = self._dag
        barneNavn = self._apnere[self._nesteApner]

        while gaveFraDag < 24:
            gaveNavn = self._kalender[gaveFraDag]

            if gaveNavn not in self._historikk[barneNavn]:
                midlertidig = self._kalender[self._dag]
                self._kalender[self._dag] = self._kalender[gaveFraDag]
                self._kalender[gaveFraDag] = midlertidig
                return True
            gaveFraDag +=1
        return False
