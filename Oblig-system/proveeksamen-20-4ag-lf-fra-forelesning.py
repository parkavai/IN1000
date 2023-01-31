# Løsningsforslaget bruker konstruksjoner fra forelesninger og
# obliger. Dersom det er gjort andre valg som virker er det ok.
# Forutsetter objektorienterte prinsipper og at oppgaven besvares.

# 4a) 5 poeng
class Emne:
    def __init__(self, emnekode, studenter, rettere):
        self._emnekode = emnekode
        self._studenter = studenter
        self._rettere = rettere
        self._obliger = {}          # {string:Oblig} Ikke gitt i oppgaven.
        
# 4b) 5 poeng
    def _skrivMeny(self):
        print ("Behandler emnet " + self._emnekode + ". Lovlige kommandoer:")
        print ("O: Ny oblig")
        print ("F: Frist ute, start retting")
        print ("L: Lag eksamensliste")
        print ("A: Avslutt")

    def administrer(self):
        self._skrivMeny()
        kommando = input("Gi kommando: ").strip().upper()
        while kommando != "A":
            if kommando == "O":
                self._opprettOblig()
            elif kommando =="F":
                self._startRetting()
            elif kommando =="L":
                self._skrivEksamensListe()
            else:
                print("Ukjent kommando.")
            self._skrivMeny()
            kommando = input("Gi kommando: ").strip().upper()

# 4g) 15 poeng - poeng gis samlet for alle tre metoder.
    def _opprettOblig(self):
        obligId = "oblig" + str(len(self._obliger)+1)
        frist = input("Oppgi frist for " + obligId + "paa formen aammdd: ")
        self._obliger[obligId] = Oblig(obligId, frist)

    def _startRetting(self):
        dagensDato = input("Oppgi dagens dato pa formen aammdd: ")
        for obligId in self._obliger:       # Noekkel er streng obligId
            oblig = self._obliger[obligId]  # Referanse til Oblig-objekt
            if oblig.klarForRetting(dagensDato):
                besvarelser = oblig.hentBesvarelser()
                resultater = oblig.fordelRetting(besvarelser, self._rettere)
                for sBruker in resultater:
                    stud = self._studenter[sBruker]
                    res = resultater[sBruker]
                    stud.registrer(obligId, res)

    def _skrivEksamensListe(self):
        eksamensliste = []
        for sBruker in self._studenter:
            stud = self._studenter[sBruker]
            if stud.altGodkjent(len(self._obliger)):
                eksamensliste.append(sBruker)
        print("Eksamensliste for emnet "+self._emnekode+":")
        for sBruker in eksamensliste:
            print(sBruker)

#4c) 10 poeng
class Student:
    def __init__(self, brukernavn, fulltNavn):
        self._bruker = brukernavn
        self._navn = fulltNavn
        self._obliger = {}
        
    def registrer(self, obligId, resultat):
        self._obliger[obligId] = resultat
        
    def altGodkjent(self, antObliger):
        if antObliger > len(self._obliger): # Noen obliger ikke levert/ registrert
            return False
        for obl in self._obliger:
            if self._obliger[obl] != 1:     # Oblig ikke godkjent
                return False
        return True
        
# 4d) 2 poeng
class Retter:
    def __init__(self, brukernavn):
        self._bruker = brukernavn
        
    def vurder(self, filnavn):
        return 1
        
# 4e) 8 poeng
class Oblig:                                # NB: Ikke besvarelser
    def __init__(self, obligId, frist):
        self._obligId = obligId
        self._frist = frist
        self._rettet = False
        
    def klarForRetting(self, dagensDato):
        return dagensDato > self._frist and not self._rettet

# Filnavn genereres i metoden ut fra entydig obligId
    def hentBesvarelser(self):
        filnavn = self._obligId + ".txt"
        alleBesvarelserFil = open(filnavn, "r") # 1 linje per student for denne oblig
        besvarelser = {}                        # {student:filnavn med besvarelse}
        for linje in alleBesvarelserFil:
            bData = linje.split()
            if len(bData) > 1:                  # kan mangle besvarelse
                besvarelser[bData[0]] = bData[1]
        alleBesvarelserFil.close()
        return besvarelser                      # alle studenters oblig-filer (1 oblig)

# 4f) 5 poeng
    def fordelRetting(self, besvarelser, rettere):
        resultater = {}
        antR = len(rettere)
        rNr = 0
        for sBruker in besvarelser:
            retter = rettere[rNr]
            res = retter.vurder(besvarelser[sBruker])
            resultater[sBruker] = res
            rNr += 1
            if rNr == antR:
                rNr = 0
            # Alternativt: rNr = (rNr + 1) % antR
        self._rettet = True
        return resultater
        
        
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