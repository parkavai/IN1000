from emne import Emne
from student import Student
from aktivitet import Aktivitet
from dato import Dato

class Undervisningsadminstrasjon:
    def __init__(self):
        self._emneordbok = {}
        self._datoordbok = {}
        self._studentordbok = {}
    
    def lesFilAktivitetEmner(self, filnavn):
        fil = open(filnavn, "r")
        for linje in fil:
            data = linje.strip().split(" ")
            emne = Emne(data[0])
            dato = Dato(data[2], data[3], data[4])
            aktivitetsnummer = int(data[1][-1])
            aktivitet = Aktivitet(emne, dato, aktivitetsnummer)
            emne.leggTilAktivitet(aktivitet)
            if(emne.hentEmneKode() not in self._emneordbok):
                self._emneordbok[data[0]] = emne
            if(dato.absoluttDato() not in self._datoordbok):
                self._datoordbok[dato.absoluttDato()] = dato
    
    def lesFilStudenter(self,filnavn):
        fil = open(filnavn, "r")
        for linje in fil:
            data = linje.strip().split(" ")
            student = Student(data[0])
            self._studentordbok[data[0]] = student
            if(data[1] in self._emneordbok):
                for aktiviteter in self._emneordbok.get(data[1]).hentAktivitet():
                    if(aktiviteter.hentAktivitetsnummer() == int(data[2][-1])):
                        aktiviteter.leggTilRegistrertStudent(student)
                        aktiviteter.registreroppmoete(student)                   
    

    def skrivGruppeMedLavtOppmoete(self,antall):
        for emner in self._emneordbok.values():
            listeAvAktiviteter = emner.hentAktivitet()
            for aktivitet in listeAvAktiviteter:
                if(aktivitet.oppmote() < antall):
                    aktivitet.skrivUtOppmoeteStudenter()
    
    def skrivUtAktiviteter(self):
        for emner in self._emneordbok.values():
            emner.skrivUt()
    

            
        

            


        