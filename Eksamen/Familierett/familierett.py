class Rett:

    def __init__(self, navn, pristall,listeAvInnhold):
        self._navn = navn
        self._pris = pristall
        self._listeAvInnhold = listeAvInnhold

    def sjekkInnholdOk(self,Innhold):
        for innholdstoff in self._listeAvInnhold:
            if innholdstoff in Innhold:
                return False
        return True

    def __str__(self):
        string = self._navn, self._pris
        for innholdstoff in self._listeAvInnhold:
            string += " " + innholdstoff
        return string

class Kategori:

    def __init__(self, kategorinavn, listeAvRetter):
        self._kategorinavn = kategorinavn
        self._listeAvRetter = listeAvRetter

    def hentOkRetter(self,Innhold):
        nyListeAvRetter = []
        for rett in self._listeAvRetter:
            if rett.sjekkInnholdOK(Innhold) == True:
                nyListeAvRetter.append(rett)
        return nyListeAvRetter

    def hentKategoriNavn(self):
        return self._kategorinavn

class Meny:

    def __init__(self, kategoriListe):
        self._kategoriListe = kategoriListe
        self._MenyOrdbok = self._lesKategoriFil(filnavn)

    def hentRedusertMeny(self,Innhold):
        nyMenyOrdbok = {}
        for kategorinavn in self._MenyOrdbok:
            if self._MenyOrdbok[kategorinavn].hentOkRetter(Innhold):
                Kategori = Kategori(kategorinavn, self._MenyOrdbok[kategorinavn])
                nyMenyOrdbok[kategorinavn] = Kategori
        return nyMenyOrdbok

class Kunde:

    def __init__(self, tlf, listeAvUnngaStoffer):
        self._tlf = tlf
        self._listeAvUnngaStoffer = listeAvUnngaStoffer

    def velgRetter(self,meny):
        menyordbok = meny
        liste = []
        for kategori in menyordbok.keys():
            print(kategori)
            rett = str(input())
            if rett != "":
                liste.append(rett)
        return liste

class Takeaway:

    def __init__(self, listeAvKategoriNavn,kundefil ):
        self._kundeKatalog = self._lesInnKundefil(kundefil)
        self._meny = Meny(listeAvKategoriNavn)

    def betjentKunde(self,tlf):
        kunde = self._kundeKatalog[tlf]
        bestilling = kunde.velgRetter(self._meny)
        self._lagOgLeverMat(bestilling)


def hovedprogram():
	mineKategorier = ["Forretter", "Hovedretter", "Desserter"]
	minTakeAway = TakeAway(mineKategorier, "kunder.txt")
	kundeId = input("Oppgi telefonnr: ")
	while kundeId != "" :
		minTakeAway.betjenKunde(kundeId)
		kundeId = input("Oppgi telefonnr: ")

hovedprogram()
