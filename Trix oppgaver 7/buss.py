class Buss:
    def __init__(self, makskapasitet):
        self._makskapasitet = makskapasitet
        self._minimumskapasitet = 0
        self._antall = 0

    def erFull(self):
        if self._antall >= self._makskapasitet:
            return True

    def plukkOpp(self):
        if self.erFull():
            print("Bussen er Full")
        else:
            print("Tok opp en passasjer")
            self._antall +=1

    def erTom(self):
        if self._antall <= self._minimumskapasitet:
            return True

    def slippAv(self):
        if self.erTom():
            print("Bussen er Tom")
        else:
            print("Slapp av en passasjer")
            self._antall -=1

    def hentAntallPassasjer(self):
         print("Det er",self._antall,"på bussen.")

def hovedprogram():
    bussen = Buss(20)
    for i in range(10):
        bussen.plukkOpp()
    bussen.hentAntallPassasjer()
    for i in range(12):
        bussen.plukkOpp()
    bussen.hentAntallPassasjer()
    for i in range(18):
        bussen.slippAv()
    bussen.hentAntallPassasjer()
    for i in range(3):
        bussen.slippAv()
    bussen.hentAntallPassasjer()
hovedprogram()
