class Bud:

    def __init__(self, budGiver, budStr):
        self._budGiver = budGiver
        self._budStr = budStr

        if self._budStr <= 0:
            self._budStr == 1

    def hentBudgiver(self):
        return self._budGiver

    def hentBudStr(self):
        return self._budStr

class Annonse:

    def __init__(self, annTekst):
        self._annTekst = annTekst
        self._budListe = []

    def hentTekst(self):
        return self._annTekst

    def giBud(self, hvem, belop):
        self._budListe.append(Bud(hvem,belop))

    def antBud(self):
        return len(self._budListe)

    def hoyesteBud(self):
        hoyeste = self._budListe[0]
        hoyeste = hoyeste.hentBudStr()
        for bud in self._budListe:
            if bud.hentBudStr() > hoyeste:
                hoyeste = bud.hentBudStr()
        for bud in self._budListe:
            if hoyeste == bud.hentBudStr():
                return hoyeste
                break

    def kraftBud(self,hvem,belop,max):
        for bud in self._budListe:
            if belop > bud.hoyesteBud().hentBudStr():
                belop = belop
            if belop > max:
                belop = bud.hoyesteBud().hentBudStr() + 1
        self._budListe.append(hvem, belop)


class Kategori:

    def __init__(self, katNavn):
        self._katNavn = katNavn
        self._annListe = []

    def nyAnnonse(self, annTekst):
        nyAnnonse = Annonse(annTekst)
        self._annListe.append(nyAnnonse)

    def hentAnnonser(self):
        return self._annListe

    def hentKategorinavn(self):
        return self._katNavn

class BruktMarked:

    def __init__(self):
        self._katListe = []

    def nyKategori(self, katNavn):
        nyKategori = Kategori(katNavn)
        for kategori in self._katListe:
            if kategori.hentKategorinavn() == katNavn:
                return None
        self._katListe.append(nyKategori)

    def finnKategori(self, katNavn):
        oppgittKategori = Kategori(katNavn)
        for kategori in self._katListe:
            if kategori.hentKategorinavn() == katNavn:
                return oppgittKategori
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
