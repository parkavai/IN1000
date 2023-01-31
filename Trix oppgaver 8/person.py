class Person:

    def __init__(self, navn):
        self._navn = navn
        self._partner = None

    def bryllup(self, nyPartner):
        self._partner = nyPartner

    def minStatus(self):
        if self._partner:
            print("Beklager, jeg er alt gift med", self._partner.hentNavn())
        else:
            print("Jeg er på sjekker'n")

    def hentNavn(self):
        return self._navn

def hovedprogram():
    mrSmith = Person("Brad Pitt")
    mrsSmith = Person("Angelina Jolie")

    mrSmith.minStatus()
    # Skal gi output: "Jeg er på sjekker'n"

    mrSmith.bryllup(mrsSmith)
    mrsSmith.bryllup(mrSmith)

    mrSmith.minStatus()
    # Skal gi output: "Beklager, jeg er alt gift med Angelina Jolie"
