class Student:
    def __init__(self, brukernavn):
        self._brukernavn = brukernavn 
        self._emner = []
    
    def sjekkEmne(self, emne):
        for e in self._emner:
            if(emne.hentEmnekode() == e.hentEmnekode()):
                return True 
        return False 

    def leggtTilEmne(self, emne):
        self._emner.append(emne)

    def hentBrukernavn(self):
        return self._brukernavn

class Emne:
    def __init__(self, emnekode):
        self._emnekode = emnekode
        self._aktiviteter = []
    
    def hentAktivitet(self, aktivitetsnummer):
        for aktivitet in self._aktiviteter:
            if(aktivitet.hentAktivitetsnummer() == aktivitetsnummer):
                return aktivitet
    
    def hentAktiviteter(self):
        return self._aktiviteter
    
    def leggTilAktiviter(self, aktivitet):
        self._aktiviteter.append(aktivitet)
    
    def hentEmneKode(self):
        return self._emnekode


class Dato:
    def __init__(self, dag, maaned, aar):
        self._dag = int(dag) 
        self._maaned = int(maaned) 
        self._aar = int(aar)
    
    def absoluttDato(self):
        maaned = str(self._maaned)
        dag = str(self._dag)
        aar = str(self._aar)
        if(len(maaned) != 2):
            maaned = "0" + maaned 
        if(len(dag) != 2):
            dag = "0" + dag
        return int(aar + maaned + dag)

    def _sjekkMaaned(self):
        if(self._maaned == 9):
            return "september"
        elif(self._maaned == 10):
            return "oktober"
        elif(self._maaned == 11):
            return "november"
        else:
            return "desember"

    def __str__(self):
        return f"{str(self._dag)}. {self._sjekkMaaned()} 20{str(self._aar)}" 

class Aktivitet:
    def __init__(self, emne, dato, aktivitetsnummer):
        self._emne = emne 
        self._dato = dato 
        self._aktivitetsnummer = aktivitetsnummer
        self._registrertliste = []
        self._oppmoeteliste = []
    
    def hentAktivitetsnummer(self):
        return self._aktivitetsnummer

    def leggTilRegistrertStudent(self, student):
        self._registrertliste.append(student)
    
    def registrerOppmoete(self, student):
        self._oppmoeteliste.append(student)
    
    def skrivUtOppmoeteStudenter(self):
        print("Alle studenter som dukket opp \n")
        for student in self._oppmoeteliste:
            print(student.hentBrukernavn() + "\n")

    def absoluttDato(self):
        return self._dato.absoluttDato()

    def oppmoete(self):
        return len(self._oppmoeteliste)

    def __str__(self):
        linje = f"Emnekode: {self._emne.hentEmneKode()} \n"
        linje += f"Aktivitetsnummmer: {self._aktivitetsnummer} \n"
        linje += f"Antall studenter møtt opp: {self.oppmoete()} \n"
        return linje 

class UndervisningsAdminstrasjon:
    def __init__(self):
        self._emneordbok = {}
        self._datoordbok = {}
        self._studentordbok = {}

    def lesInnEmner(self, filnavn):
        fil = open(filnavn, "r")
        for linje in fil:
            alledata = linje.strip().split()
            emnekode = alledata[0] 
            tmp = alledata[1]
            aktivitetsnummer = tmp[-1]

            if(emnekode not in self._emneordbok):
                nyemne = Emne(emnekode)
                self._emneordbok[emnekode] = nyemne

            emne = self._emneordbok[emnekode]
            dato = Dato(alledata[2], alledata[3], alledata[4])

            if(dato.absoluttDato() not in self._datoordbok):
                self._datoordbok[dato.absoluttDato()] = dato 

            aktivitet = Aktivitet(emne, dato, aktivitetsnummer)
            emne.leggTilAktiviteter(aktivitet)
    
    def lesInnStudenter(self, filnavn):
        fil = open(filnavn, "r")
        for linje in fil:
            alledata = linje.strip().split()
            brukernavn = alledata[0]
            emnekode = alledata[1]
            tmp = alledata[2]
            aktivitetsnummer = tmp[-1]

            if(brukernavn not in self._studentordbok):
                nystudent = Student(brukernavn)
                self._studentordbok[brukernavn] = nystudent

            student = self._studentordbok[brukernavn]
            emne = self._emneordbok[emnekode]

            if(student.sjekkEmne(emne) == False):
                student.leggTilEmne(emne)
            
            aktivitet = emne.hentAktivitet(aktivitetsnummer)
            aktivitet.leggTilRegistrertStudent(student)
            aktivitet.registrerOppmoete(student)
    
    def skrivGrupperMedLavtOppmoete(self, antall):
        for e in self._emneordbok:
            emne = self._emneordbok[e]
            for aktivitet in emne.hentAktiviteter():
                if(aktivitet.oppmoete() < antall):
                    print(aktivitet)
        
def hovedprogram():
    dato1 = Dato(19, 11, 20)
    print(dato1)
    print(dato1.absoluttDato())

hovedprogram()