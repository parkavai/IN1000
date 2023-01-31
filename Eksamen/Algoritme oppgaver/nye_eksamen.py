class Emne:
    def __init__(self, emnekode, emnenavn):
        self._emnekode = str(emnekode)
        self._emnenavn = str(emnenavn) 
        self._eier = None

    def leggTilEier(self, institutt):
        self._eier = institutt
    
    def hentEmneKode(self):
        return self._emnekode
        
    def __str__(self):
        linje = ""
        if(self._eier != None):
            linje += "Institutt: " + self._eier.hentInstituttNavn() + "\n"
        linje += "Emnekode: " + self._emnekode + "\n"
        linje += "Navnet på emnet: " + self._emnenavn + "\n"
        return linje
    
class Studieprogram:
    def __init__(self, program):
        self._emneliste = []
        self._program = str(program)
    
    def hentEmneListe(self):
        return self._emneliste
    
    def hentProgramNavn(self):
        return self._program
    
    def leggTilEmne(self, emne):
        for e in self._emneliste:
            if(emne.hentEmneKode() == e.hentEmneKode()):
                return
        self._emneliste.append(emne)
    
    def __str__(self):
        text = ""
        text += "Studieprogrammet: " + self._program + "\n"
        for emne in self._emneliste:
            text += emne.__str__()
        return text

class Institutt:
    def __init__(self, institutt_navn, listeAvStudieprogram, emneordbok):
        self._institutt_navn = str(institutt_navn)
        self._listeAvStudieprogram = listeAvStudieprogram
        self._emneordbok = emneordbok
        self.fyllInnEmneOrdbok()
    
    def fyllInnEmneOrdbok(self):
        for studieprogram in self._listeAvStudieprogram:
            for emne in studieprogram.hentEmneListe():
                if(emne.hentEmneKode() not in self._emneordbok):
                    self._emneordbok[emne.hentEmneKode()] = emne
                    self.leggTilEier(emne)
                    
    def hentInstituttNavn(self):
        return self._institutt_navn
    
    def printProgram(self):
        for studieprogram in self._listeAvStudieprogram:
            print(studieprogram)
    
    def leggTilStudieprogram(self, studieprogram):
        for sp in self._listeAvStudieprogram:
            if(sp.hentProgramNavn() == studieprogram.hentProgramNavn()):
                return
        self._listeAvStudieprogram.append(studieprogram)
    
    def leggTilEmne(self, emne):
        if(emne.hentEmneKode() not in self._emneordbok):
            self.leggTilEier(emne)
            self._emneordbok[emne.hentEmneKode()] = emne 
    
    def leggTilEier(self, emne):
        emne.leggTilEier(self)

def hovedprogram():
    intro_objektorientert = Emne("IN1000", "Introduksjon til objektorientert programmering")
    objektorientert_prog = Emne("IN1010", "Objektorientert programmering")
    logiske_met = Emne("IN1150", "Logiske metoder")
    intro_design = Emne("IN1050", "Introduksjon til design")
    
    prosa = Studieprogram("Programmering og systemarkitektur")
    design = Studieprogram("Design, bruk, interaksjon")
    
    prosa.leggTilEmne(intro_objektorientert)
    prosa.leggTilEmne(objektorientert_prog)
    
    design.leggTilEmne(intro_objektorientert)
    design.leggTilEmne(objektorientert_prog)

    prosa.leggTilEmne(logiske_met)
    design.leggTilEmne(intro_design)

    print(prosa)
    print(design)
    
# Sjekke at når man printer emner, så skal ikke eiernavnet inkluderes ettersom vi ikke har satt eier
# for emnene over
    print(intro_objektorientert)
    print(logiske_met)
    
# Tildeler eier for alle emner
    listeAvStudieprogram = []
    listeAvStudieprogram.append(prosa)
    listeAvStudieprogram.append(design)
    informatikk_institutt = Institutt("Informatikk", listeAvStudieprogram, {})
    informatikk_institutt.leggTilEmne(intro_objektorientert)
    informatikk_institutt.leggTilEmne(logiske_met)

# Sjekker om eier er tilordnet gjennom å printe ut emne
    print(intro_objektorientert)
    print(logiske_met)
    
# Lager ny institutt for å sjekke at eier er blitt endret for emner
    matte_institutt = Institutt("Matematikk", listeAvStudieprogram, {})
    matte_institutt.leggTilEmne(intro_objektorientert)
    matte_institutt.leggTilEmne(logiske_met)

# Sjekker om eier er blitt endret for begge emnene under 
    print(intro_objektorientert)
    print(logiske_met)

    informatikk_institutt.leggTilEier(intro_objektorientert)
    print(intro_objektorientert)
    informatikk_institutt.printProgram()
    

hovedprogram()