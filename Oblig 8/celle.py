class Celle:
# Konstruktør
    def __init__(self):
        self.status = "død"

    # Metodene endrer status til cellen.
    def settDoed(self):
        self.status = "død"

    def settLevende(self):
        self.status = "levende"

    # Henter statusen til cellen og ser om den er levende eller ikke.
    def erLevende(self):
        if self.status == "levende":
            return True
        else:
            return False

    # Ser om statusen er levende eller ikke og returnerer tegnrepresentasjon for den cellen.
    def hentStatusTegn(self):
        if self.erLevende():
            return "O";
        else:
            return "."
