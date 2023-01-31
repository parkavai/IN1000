class Student:

    def __init__(self, brukernavn):
        self._studentnavn = brukernavn
        self._emner = []

    def hentBrukernavn(self):
        return self._studentnavn

    def leggTilAktivitetEmne(self,emne):
        # Emne inneholder også aktiviteter
        self._emner.append(emne)

class Emne:

    def __init__(self, emneKode):
        self._aktiviter = []
        self._emneKode = emneKode

    def leggTilAktivitet(self, aktivitet):
        self._aktiviter.append(aktivitet)

class Dato:

    def __init__(self, dag, maaned, aar):
        self._dag = dag
        self._maaned = maaned
        self._aar = aar

    def absoluttDato(self):
        if int(self._dag) < 10:
            self._dag = str(0) + str(self._dag)
        if int(self._maaned) < 10:
            self._maaned = str(0) + str(self._maaned)
        if int(self._aar) < 10:
            self._aar = str(0) + str(self._aar)
        dato =  str(self._aar) + str(self._maaned) + str(self._dag)
        return int(dato)


    def __str__(self):
        if self._maaned == 9:
            return (str(self._dag) + ".", "september","20" + str(self._aar))
        elif self._maaned == 10:
            return (str(self._dag) + ".", "oktober","20" + str(self._aar))
        elif self._maaned == 11:
            return (str(self._dag) + ".", "november","20" + str(self._aar))
        elif self._maaned == 12:
            return (str(self._dag) + ".", "desember","20" + str(self._aar))
        else:
            return ("Denne måneden gjelder ikke for hoestsemesteret")

class Aktivitet:

    def __init__(self, emne, dato, aktivitetsnummer):
        self._emneObjekt = emne
        self._datoObjekt = dato
        self._aktivitetsnummer = aktivitetsnummer
        self._registrertStudentweb = []
        self._oppmoeteRegister = []

    def leggTilRegisterStudent(self, student):
        self._registrertStudentweb.append(Student(student))

    def registrerOppmote(self, student):
        self._oppmoeteRegister.append(Student(student))

    def skrivUtOppmote(self):
        for studenter in self._oppmoeteRegister:
            studenter.hentBrukernavn()

    def absoluttDato(self):
        return self._datoObjekt.absoluttDato()

    def oppmote(self):
        return len(self._oppmoeteRegister)

    def __str__(self):
        return self._emneObjekt, self._aktivitetsnummer, len(self._oppmoeteRegister)

class Undervisningsadminstrasjon:

    def __init__(self):
        self._emneOrdbok = {}
        self._datoOrdbok = {}
        self._studentOrdbok = {}

    def lesInnEmneAktivitetFil(filnavn):
        fil = open(filnavn, "r")
        for data in fil:
            data = data.strip().split()
            emneKode = data[0]
            aktivitet = data[1]
            dato = Dato((data[2]) + (data[3]) + (data[4]))
            emneObjekt = Emne(emneKode)
            emneObjekt.leggTilAktivitet(Aktivitet(emneKode,aktivitet,dato))
            self._emneOrdbok[emneKode] = emneObjekt
            self._datoOrdbok[dato.absoluttDato()] = dato

    def lesInnStudentEmner(filnavn):
        fil = open(filnavn, "r")
        for data in fil:
            data = data.strip().split()
            brukernavn = data[0]
            emneKode = data[1]
            aktivitet = data[2]
            student = Student(brukernavn)
            mittEmne = self._emneOrdbok[emneKode]
            student.leggTilAktivitetEmne(mittEmne)
            self._studentOrdbok[brukernavn] = student


    def skrivGrupperMedLavtOppmoete(self,antall):
        for emneObjekt in self._emneOrdbok.values():
            if emneObjekt.oppmote() < antall:
                emneObjekt.skrivUtOppmote()








test = str(12) + str(12) + str(22)
variabel = "9"
variabel = "0" + variabel
print(variabel)
Dato = Dato(4, 11, 2020);
Dato2 = Dato.absoluttDato();
print(Dato2);
test2 = int(test);
if int(10) == 10:
    print("ja");

print("test2",test2)
