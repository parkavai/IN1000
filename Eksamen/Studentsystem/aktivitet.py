class Aktivitet:
    def __init__(self,emne, dato, aktivitetsnummer):
        self._emne = emne
        self._dato = dato
        self._aktivitetsnummer = aktivitetsnummer
        self._studentweb = []
        self._oppmoteregistrering = []
    
    def leggTilRegistrertStudent(self,student):
        self._studentweb.append(student)

    def registreroppmoete(self, student):
        self._oppmoteregistrering.append(student)
    
    def hentAktivitetsnummer(self):
        return self._aktivitetsnummer
    
    def skrivUtOppmoeteStudenter(self):
        print("Studenter som møtte opp til " + str(self._emne.hentEmneKode()) + " med dato: " + self._dato.absoluttDato())
        for studenter in self._oppmoteregistrering:
            print(studenter.hentBrukernavn())
        print("\n")
    
    def absoluttDato(self):
        return self._dato.absolutDato()
    
    def oppmote(self):
        return len(self._oppmoteregistrering)
    
    def __str__(self):
        linje = "Emne: " + str(self._emne.hentEmneKode()) + "\n"
        linje += "Aktivitetsnummer: " + str(self._aktivitetsnummer) + "\n"
        linje += "Antall som møtte opp: " + str(self.oppmote()) + "\n"
        return linje
