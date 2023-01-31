from aktivitet import Aktivitet

class Emne:

    def __init__(self,emnekode):
        self._emnekode = emnekode
        self._aktiviteter = []
    
    def leggTilAktivitet(self,aktivitet):
        self._aktiviteter.append(aktivitet)
    
    def hentEmneKode(self):
        return self._emnekode
    
    def hentAktivitet(self):
        return self._aktiviteter
    
    def skrivUt(self):
        for aktiviteter in self._aktiviteter:
            print(aktiviteter)

    

        