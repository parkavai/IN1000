class Oblig:

    def __init__(self, oblig,frist):
        self._oblig = oblig
        self._frist = frist
        self._rettet = False

    def klarForRetting(self,dato):
        if dato > self._frist and self._rettet != False:
            return True
        else:
            return False

    def hentBesvarelser(self,filnavn):
        filnavn = self._oblig + ".txt"
        alleBesvarelserFil = open(filnavn, "r")
        besvarelser = {}
        for linje in alleBesvarelserFil:
            biter = linje.split()
            besvarelser[biter[0]] = biter[1]
        alleBesvarelserFil.close()
        return besvarelser
