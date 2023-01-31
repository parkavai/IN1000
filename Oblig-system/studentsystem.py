
from unittest import result


class Emne:
    def __init__(self, emnekode, studentOrdbok, retterListe):
        self._emnekode = str(emnekode)
        self._studentOrdbok = studentOrdbok
        self._retterListe = retterListe
        self._obligListe = {}
        self._id = 0
    
    def _oekId(self):
        self._id += 1
    
    def skrivMeny(self):
        meny = f'Emnekode: {self._emnekode} \n'
        meny += f'Oversikt over ulike kommandoer \n'
        meny += f'Oversikt over ulike kommandoer \n'
        meny += 'O: Ny oblig \n'
        meny += 'F: Frist ute, start retting \n'
        meny += 'L: Lag eksamensliste \n'
        meny += 'A: Avslutt \n'
        print(meny)

    def adminstrer(self):
        self._skrivMeny()
        brukerInput = str(input("Tast inn kommando: ").strip().upper())
        while (brukerInput != 'A'):
            if(brukerInput == 'O'):
                self._opprettoblig()
            elif(brukerInput == 'F'):
                self._startRetting()
            elif(brukerInput == 'L'):
                self._skrivEksamensliste()    
            else:
                print("Tastet inn ugyldig kommando, se under")
            self._skrivMeny()
            brukerInput = str(input("Tast inn kommando: ").strip().upper())

    
    def _opprettOblig(self):
        obligId = self._id 
        self._oekId()
        leveringsFrist = str(input("Tast inn leveringsfrist"))
        self._obligListe[obligId] = Oblig(obligId, leveringsFrist)

    def _startRetting(self):
        dagensDato = str(input("Tast inn dagens dato"))
        for nokkel in self._obligListe:
            oblig = self._obligListe[nokkel]
            if(oblig.klarForRetting(dagensDato) != True):
                studentOrdbok = oblig.hentBesvarelser()
                resultatOrdbok = oblig.fordelRetting(studentOrdbok, self._retterListe)
                for brukernavn in resultatOrdbok:
                    besvarelse = resultatOrdbok[brukernavn]
                    self._studentOrdbok[brukernavn] = besvarelse
                    stud = self._studentOrdbok[brukernavn]
                    stud.registrer(nokkel, besvarelse)

    def _skrivEksamensListe(self):
        eksamensliste = []
        for sBruker in self._studenter:
            stud = self._studenter[sBruker]
            if stud.altGodkjent(len(self._obliger)):
                eksamensliste.append(sBruker)
        print("Eksamensliste for emnet "+self._emnekode+":")
        for sBruker in eksamensliste:
            print(sBruker)

class Student:
    def __init__(self, brukernavn, fulltNavn):
        self._brukernavn = brukernavn 
        self._fulltNavn = fulltNavn
        self._obligOrdbok = {}
    
    def registrer(self, obligId, resultat):
        self._obligOrdbok[obligId] = resultat 
    
    def altGodkjent(self, antObliger):
        i = 0
        for resultat in self._obligOrdbok:
            if(resultat != 1):
                return False 
            i += 1
        if(i != antObliger):
            return False 
        return True 

class Retter:
    def __init__(self, brukernavn):
        self._brukernavn = brukernavn
    
    def vurder(self, filnavn):
        return 1 

class Oblig:
    def __init__(self, obligId, leveringsFrist):
        self._obligId = obligId
        self._leveringsFrist = leveringsFrist
        self._rettet = False
    
    def _formaterLeveringsFrist(self, dato):
        return dato[0:2] + ":" + dato[2:4] + ":" + dato[4:6]
    
    def klarForRetting(self, dagensDato):
        aar = int(self._leveringsFrist[0:2])
        maaned = int(self._leveringsFrist[2:4])
        dag = int(self._leveringsFrist[4:6])

        #frist = self._formaterLeveringsFrist(self._leveringsFrist).strip().split(":")
        #dagens = self._formaterLeveringsFrist(dagensDato).strip().split(":")
        if (aar <= int(dagensDato[0:2])) and (maaned <= int(dagensDato[2:4])) and (dag <= int(dagensDato[4:6]) and self._rettet == False):
            return True 
        else:
            return False 
    
    def hentBesvarelser(self):
        filnavn = self._obligId + ".txt"
        fil = open(filnavn, "r")
        ordbok = {}
        for linje in fil:
            alledata = linje.strip().split()
            student = str(alledata[0])
            studentbesvarelse = str(alledata[1])
            ordbok[student] = studentbesvarelse
        fil.close()
        return ordbok 
    
    def fordelRetting(self, studentOrdbok, retterListe):
        resultatOrdbok = {}
        i = 0
        for nokkel in studentOrdbok:
            besvarelse = studentOrdbok[nokkel]
            retter = retterListe[i]
            res = retter.vurder(besvarelse)
            resultatOrdbok[nokkel] = res
            i += 1
            if(i == len(retterListe[i])):
                i = 0
        self._rettet = True 
        return resultatOrdbok

            
        
# Hovedprogram er ikke gitt i oppgaven og skulle ikke skrives.
# Eksempel, ikke komplett testprogram.
def hovedprogram():
    # emnekode = input("Hvilket emne skal administreres? ")
    studenter = {}
    for i in range(1, 5):   # Genererer data med "kjedelige" navn
        brukernavn = "s"+str(i)
        ny = Student(brukernavn, "Fulltnavn student: " + brukernavn)
        studenter[brukernavn] = ny

    rettere = []
    for i in range(1,3):   # Genererer data med "kjedelige" navn
        nyR = Retter("R"+str(i))
        rettere.append(nyR)
    

    emne = Emne("IN1000", studenter, rettere)
    emne.administrer()
    print("Programmet avsluttes")

hovedprogram()        

    

    