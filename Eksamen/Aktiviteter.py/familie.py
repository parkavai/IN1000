class Aktivitet:

    def __init__(self, hva,kl):
        self._aktNavn = hva
        self._start = kl

    def visAktivitet(self):
        print("Aktiviteten starter kl: ", self._start)
        print("Følgende aktivitet er: ", self._aktNavn)


class Ukedag:

    def __init__(self, dag):
        self._dag = dag
        self._aktiviteter = []
        for timer in range(0,24):
            self._aktiviteter.append(None)

    def settInn(self, hva, kl):
        if self._aktiviteter[kl] is not None:
            print("Klokkeslettet er opptatt.")
        else:
            self._aktiviteter[kl] = Aktivitet(hva, kl)

    def tidligste(self):
        for i in range(0, 24):
            if self._aktiviteter[i] is not None:
                return i
        return -1


    def seneste(self):
        sum = 0
        for i in range(0, 24):
            if self._aktiviteter[i] is not None:
                sum +=1
            return sum
        return -1

    def antall(self):
        sum = 0
        for i in range(0, 24):
            if self._aktiviteter[i] is not None:
                sum +=1
        return sum

    def settInnLedig(self, hva):
        ingen = True
        ferdig = False
        for i in range(0, 24):
            if self._aktiviteter[i] is not None:
            ingen = False
        if ingen:
            self.settInn(hva, 12)
            ferdig = True

        if not ferdig:
            for i in range(self.tidligste() + 1, self.seneste()):
                if self._aktiviteter[i] is None:
                self.settInn(hva, i)
                ferdig = True

        if not ferdig:
            for i in range(self.seneste() + 1, 24):
                if self._aktiviteter[i] is None:
                self.settInn(hva, i)
                ferdig = True

        if not ferdig:
            for i in range(self.tidligste(), -1, -1):
                if self._aktiviteter[i] is None:
                self.settInn(hva, i)
                ferdig = True

        if not ferdig:
            print("Det er ikke plass til aktiviteten paa denne dagen!")

    def skrivUt(self):
        print(self._dag + ":")
            for akt in self._aktiviteter:
                if akt is not None:
                    print(" ", akt)

class Ukeplan:
    def __init__(self, hvem):
    self._hvem = hvem
    self._dager = [ Ukedag("Mandag"), Ukedag("Tirsdag"), Ukedag("Onsdag"),
                    Ukedag("Torsdag"), Ukedag("Fredag"), Ukedag("Lordag"),
                    Ukedag("Sondag") ]

    def travleste(self):
        maks = 0
        for i in range(0, 7):
            if self._dager[i].antall() > self._dager[maks].antall():
                maks = i
        return self._dager[maks]

    def skrivUt(self):
        print("Ukeplan for " + self._hvem + ":")
        for dag in self._dager:
            dag.skrivUt()

    def __str__(self):
    return "Kl " + str(self._start) + ": " + self._aktNavn


class Familie:
    def __init__(self):
        self._ukeplaner = []

    def skrivAktiviteter(self):
        print("Aktiviteter:")
        skrevet = {}
        for plan in self._ukeplaner:
            for dag in plan.hentUkedager():
                for akt in dag.hentAktiviteter():
                    if akt is not None and akt.hentNavn() not in skrevet:
                    print(akt)
                    skrevet[akt.hentNavn()] = True

    def hentUkedager(self):
        return self._dager

    def hentAktiviteter(self):
        return self._aktiviteter

    def hentNavn(self):
        return self._aktNavn
