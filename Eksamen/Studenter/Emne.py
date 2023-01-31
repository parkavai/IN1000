class Emne:

    def __init__(self, emnekode,studenter,rettere):
        self._emnekode = str(emnekode)
        self._studentordbok = studenter
        self._rettere = rettere
        self._obliger = {}

    def adminstrer(self):
        print("Her er emnekoden for ditt emne: ", self._emnekode)
        print("")
        print("Under er oversikten over de følgende kommandoene: ")
        print("O: For å opprette en oblig")
        print("F: Fristen er ute og igangsetter retting av oblig")
        print("L: Lager eksamensliste")
        print("A: Avslutter løkken")
        print()
        print()

        inp = str(input("Skriv inn kommandoene over: "))
        brukerinput = inp.upper().strip()

        while brukerinput != "A":
            if brukerinput == "O":
                self._opprettOblig()
            elif brukerinput == "F"
                self._startRetting()
            elif brukerinput == "L"
                self._skrivEksamensliste()
            else:
                print("Oppstod en feil, husk å tast inn kommandoene vist over")
            brukerinput = inp.upper().strip()
