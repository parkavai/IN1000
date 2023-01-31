class Bok:

    def __init__(self, tittel, utgivelsesaar, forfatter):
        self._tittel = tittel
        self._utgivelsesaar = int(utgivelsesaar)
        self._forfatter = forfatter

    def hentNavn(self):
        return self._tittel

    def hentUtgivelsesaar(self):
        return self._utgivelsesaar

    def printBok(self):
        print(self._tittel + " - " + self._forfatter + " - " +  str(self._utgivelsesaar))

class Bokhylle:

    def __init__(self, maksplass):
        self._maksplass = int(maksplass)
        self._boker = []

    def erDetPlass(self):
        if len(self._boker) != self._maksplass:
            return True
        else:
            return False

    def leggTilBok(self,bok):
        if self.erDetPlass() == True:
            self._boker.append(bok)
            return True
        else:
            return False

    def finnBok(self,navn,utgivelsesaar):
        for i in self._boker:
            if navn == i.hentNavn() and utgivelsesaar == i.hentUtgivelsesaar():
                return True
        return False

    def printBokhylle(self):
        for bok in self._boker:
            bok.printBok()

class Bibliotek:
    bokHylleListe = []
    standardBokhylleStorrelse = None

    def __init__(self, standardBokhylleStorrelse = 5):
        self.standardBokhylleStorrelse = standardBokhylleStorrelse
        self.bokHylleListe = [] # Starter med et tomt bibliotek

    def leggTilBokIBibliotek(self, boken):
        # Har ikke plass til det motsatte er bevist
        ledigBokhylle = None

        # Sjekk om det finnes plass i en bokhylle
        for bokhylle in self.bokHylleListe:
            erPlass = bokhylle.erDetPlass()
            if erPlass:
                ledigBokhylle = bokhylle

        if ledigBokhylle == None:
            # Vi har ikke en ledig bokhylle tilgjengelig
            # Må lage en selv
            ledigBokhylle = self.utvidBibliotek()

        # Nå vet vi at vi har en bokhylle tilgjengelig
        ledigBokhylle.leggTilbok(boken)

    def utvidBibliotek(self):
        # Lag en ny bokhylle
        nyBokhylle = Bokhylle(self.standardBokhylleStorrelse)

        # Legg til bokhyllen i vår bokhylleliste
        self.bokHylleListe.append(nyBokhylle)
        # Returnerer den nye bokhyllen
        return nyBokhylle

    def finnBokIBibliotek(self, boken):
        bokNavn = boken.navn
        utgAar = boken.utgivelsesaar

        # Sjekk om det finnes plass i en bokhylle
        for bokhylle in self.bokHylleListe:
            returnertBok = bokhylle.finnBok(bokNavn, utgAar)
            # returnertBok er enten en bok eller False

            if returnertBok != False:
                # Hvis returnertBok ikke er False, må det være en bok
                return returnertBok

    def printBibliotek(self):
        counter = 1
        print("Antall hyller: " + str(len(self.bokHylleListe)))
        for hylle in self.bokHylleListe:
            print("Bokhylle nr. " + str(counter))
            hylle.printBokhylle()
            print("\n")
            counter += 1


enBok = Bok("Dracula on new Adventures", 1996, "Dr. Dracula")
biblio = Bibliotek()

biblio.leggTilBokIBibliotek(enBok)

biblio.printBibliotek()
