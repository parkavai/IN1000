from kategori import Kategori

class Meny:
    def __init__(self, listeAvKategoriNavn):
        self._menyOrdbok = self._lesKategoriFil(".txt")
    
    def _lesKategoriFil(filnavn):
        return None
    
    def hentRedusertMeny(self,unngainnholdstofferliste):
        for kategorier in self._menyOrdbok:
            if (self._menyOrdbok[kategorier].hentOkRetter(unngainnholdstofferliste).len() != 0):
                self._menyOrdbok[kategorier] = self._menyOrdbok[kategorier].hentOkRetter(unngainnholdstofferliste)
        return self._menyOrdbok
        
            
            
        

    

        