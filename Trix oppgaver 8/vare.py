class Vare:

    def __init__(self, beskrivelse):
        self._beskrivelse = beskrivelse
        self._hoyesteBud = None

    def by(self, pris):
        bud = int(pris)
        if bud > self._hoyesteBud:
            self._hoyesteBud = bud

    def seBud(self):
        if self._hoyesteBud is None:
            print("Ingen har lagt ut bud på varen!")
            return 0
        return self._hoyesteBud
