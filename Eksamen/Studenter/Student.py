class Student:

    def __init__(self, fornavn,etternavn):
        self._fornavn = fornavn
        self._etternavn = etternavn
        self._brukernavn = None
        self._obliger = {}

    def lagBrukernavn(self):
        self._brukernavn = self._fornavn + self._etternavn[0]

    def hentBrukernavn(self):
        return self._brukernavn

    def registrer(self,oblig,resultat):
        self._obliger[oblig] = resultat

    def altGodkjent(self,antObliger):
        if len(self._obliger) < antObliger:
            return False
        for i in self._obliger:
            resultatet = self._obliger[i]
            if resultatet == 1:
                return True
        return False
