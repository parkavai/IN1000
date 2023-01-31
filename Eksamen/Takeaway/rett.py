class Rett:
    def __init__(self,navn, pris, listeAvInnholdsstoffer):
        self._navn = str(navn)
        self._pris = float(pris)
        self._listeAvInnholdsstoffer = listeAvInnholdsstoffer
    
    def sjekkinnholdOK(self,annenListe):
        for x in self._listeAvInnholdsstoffer:
            for y in annenListe:
                if(x == y):
                    return False
        return True
    
    def __str__(self):
        utskrift = "Rett: " + self._navn + "\n"
        utskrift += "Pris: " + str(self._pris) + "\n"
        utskrift += "Inneholder:  \n"
        for stoff in self._listeAvInnholdsstoffer:
            utskrift += stoff + "\n"
        return utskrift
    

    