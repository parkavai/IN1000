class Bud:
    def __init__(self, navn,budstoerrelse):
        self._budgiver = str(navn)
        self._budStr = int(budstoerrelse)
        self._bud = []

    def endreBudStr(self):
        if self._budStr <= 0:
            self._budStr = 1

    def hentBudgiver(self):
        return self._budgiver

    def hentBudStr(self):
        return self._budStr

class Annonse:
    def __init__(self, annTekst):
        self._anntekst = annTekst
        self._bud = []

    def hentTekst(self):
        return self._anntekst

    def giBud(self,hvem,belop):
        self._bud.append(Bud(hvem,belop))

    def antBud(self):
        return len(self._bud)

    def hoyestebud(self):
        hoyesteVerdi = 0
        for bud in self._bud:
            if bud.hentBudStr() > hoyesteVerdi:
                hoyesteVerdi = bud.hentBudStr()
        for bud in self._bud:
            if hoyesteVerdi == bud.hentBudStr():
                break
        return hoyesteVerdi

    def kraftBud(self,hvem,belop,max):
        hoyeste = self.hoyesteBud().hentBudStr()
        if hoyeste < belop:
            belop = hoyeste + 1

        if belop > max:
            belop = max

        self.giBud(hvem, budBelop)


class Kategori:
    def __init__(self, katNavn):
        self._katnavn = katNavn
        self._annonseliste = []

    def nyAnnonse(self, annTekst):
        nyAnn = Annonse(annTekst)
        self._annonseliste.append(nyAnn)

    def hentAnnonser(self):
        return self._annonseliste

class BruktMarked:
    def __init__(self):
        self._kategori = {}

    def nyKategori(self, katNavn):
        if katNavn in self._kategori:
            return None
        else:
            self._kategori[katNavn] = Kategori(katNavn)

    def finnKategori(self, katNavn):
        if katnavn in self._kategori:
            return self._kategori[katNavn]
        else:
            return None

def hovedprogram():
    marked = BruktMarked()
    #metoden nyKategori returnerer den nye kategorien vaar
    kat = marked.nyKategori("sykkellykt")
    ann = kat.nyAnnonse("New York sykkellykt")
    ann.giBud("Peter", 42)
    ann.giBud("Ann", 0)
    ann.kraftBud("Mary", 40, 50)
    hoyesteBudStr = ann.hoyesteBud().hentBudStr()
    budGiver = ann.hoyesteBud().hentBudgiver()
    #sjekker at utskriften gir 43 gitt av Mary
    print(hoyesteBudStr, "gitt av", budGiver )
    #alternativt med assert:
    assert hoyesteBudStr == 43
    assert budGiver == "Mary"
hovedprogram()
