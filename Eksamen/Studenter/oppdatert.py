# Løsningsforslaget bruker konstruksjoner fra forelesninger og
# obliger. Dersom det er gjort andre valg som virker er det ok.
# Forutsetter objektorienterte prinsipper og at oppgaven besvares.
# Poengfordelingen er veiledende og indikerer vekting - bruk skjønn.


# 4a) 5 poeng
# 2 poeng for initiering av emnekode, studenter og rettere
# 2 poeng for opprettelse av tom ordbok til obliger (evt liste)
# 1 poeng for helhet
class Emne:
    def __init__(self, emnekode, studenter, rettere):
        self._emnekode = emnekode
        self._studenter = studenter
        self._rettere = rettere
        self._obliger = {}

# 4b) 5 poeng
# Ok med hjelpemetode men ikke noe trekk om alt i en metode
    def _skrivMeny(self):
        print ("Behandler emnet " + self._emnekode + ". Lovlige kommandoer:")
        print ("O: Ny oblig")
        print ("F: Frist ute, start retting")
        print ("L: Lag eksamensliste")
        print ("A: Avslutt")

# 2 poeng for korrekt utskrift med emnenavn og meny
# (jeg tenkte meg en input-løkke her, men ikke eksplisitt så ikke krav)
# 2 poeng for input test m/ håndtering av blanke og case
# 1 poeng for korrekt kall på metoder, uten argumenter
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
# 6 p - Objektorientering:
#   overordnet design, innkapsling, metodekall kun på objekter, fornuftig bruk
#   av andre metoder i samme og andre klasser, bruk av instansvariable (ikke
#   parametere til metodene) internt i klassen
# 5 p - Logikk: Løsning som fungerer, inkl generert unike obligId
# 4 p - Syntaks og semantikk forøvrig, som oppslag og oppbygging av ordbøker
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
# __init__ : 2 poeng, spesielt ordbok for obliger
# registrer: 3 poeng, korrekt innsetting i ordbok
# altGodkjent: 4 poeng, NB test på antall OG hver enkelt oblig
# Helhet inkl parametere: 1 poeng
class Student:
    def __init__(self, brukernavn, fulltNavn):
        self._bruker = brukernavn
        self._navn = fulltNavn
        self._obliger = {}

    def registrer(self, obligId, resultat):
        self._obliger[obligId] = resultat

    def altGodkjent(self, antObliger):
        if antObliger > len(self._obliger):
            return False
        for obl in self._obliger:
            if self._obliger[obl] != 1:
                return False
        return True

# 4d) 2 poeng
class Retter:
    def __init__(self, brukernavn):
        self._bruker = brukernavn

    def vurder(self, filnavn):
        return 1

# 4e) 8 poeng
# __init__: 1 poeng for initiering av boolsk instansvariabel
# klarForRetting: 2 poeng, int- og string-dato er begge ok
#   (men konsistent)
# hentBesvarelser: 4 poeng for filhåndtering. Ikke trekk for
#   manglende sjekk på besvarelse på en linje, men for studenter
#   som sjekker kan det kompensere med 1-2 poeng for andre
#   mangler i deloppgaven, spes hvis de har fått problemer
#   med å håndtere ikke-leverte besvarelser.
# annet/ helhet: 1 poeng
class Oblig:
    def __init__(self, obligId, frist):
        self._obligId = obligId
        self._frist = frist
        self._rettet = False

    def klarForRetting(self, dagensDato):
        return dagensDato > self._frist and not self._rettet

# Filnavn genereres i metoden ut fra entydig obligId, ellers -1
# Om de har en annen løsning som virker og "makes sense" trekkes det ikke.
    def hentBesvarelser(self):
        filnavn = self._obligId + ".txt"
        alleBesvarelserFil = open(filnavn, "r")
        besvarelser = {}
        for linje in alleBesvarelserFil:
            bData = linje.split()
            if len(bData) > 1:
                besvarelser[bData[0]] = bData[1]
        alleBesvarelserFil.close()
        return besvarelser

# 4f) 5 poeng
# Dette er tenkt som en A(B)-oppgave
# Sjekk at oblig-repr er konsistent (liste eller ordbok)
# 3 poeng: Korrekt logikk inkl oppdatering _rettet. Flere fremgangsmåter ok men
#   -1 for spesielt tungvint
#   -2 poeng for direkte aksess av instansvariabler (ikke via metode)
# 2 poeng: Traversering og aksess av liste/ ordbøker, inkl at
# vurder kalles på Retter-objekt, ikke string
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
# Eksempel, ikke testprogram.
def hovedprogram():
    emner = {}
    emnekode = input("Oppgi emnekode (avslutt med 'Q')? ").strip().upper()
    while emnekode[0] != "Q":
        # evt sjekk på om format er korrekt
        if emnekode not in emner:
            r1 = Retter("pr")
            r2 = Retter("kr")
            rettere = [r1, r2]
            studenter = {"mtt":Student("mtt", "mette"), "spn":Student("spn", "espen"), "frdrk":Student("frdrk", "fredrik")}
            emner[emnekode] = Emne(emnekode, studenter, rettere)
        emner[emnekode].administrer()
        emnekode = input("Oppgi emnekode (avslutt med 'Q')? ").strip().upper()

    print("Emneadministrasjon avsluttes")

hovedprogram()
