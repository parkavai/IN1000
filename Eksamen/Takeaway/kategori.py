from rett import Rett

class Kategori:
    def __init__(self,kategorinavn, listeAvRetter):
        self._kategorinavn = kategorinavn
        self._listeAvRetter = listeAvRetter
    
    def hentOkRetter(self,unngaainnholdsliste):
        nyListe = []
        for retter in self._listeAvRetter:
            if(retter.sjekkinnholdOK(unngaainnholdsliste) != False):
                nyListe.append(retter)
        return nyListe

        