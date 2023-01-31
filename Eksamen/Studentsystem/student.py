class Student:

    def __init__(self, brukernavn):
        self._brukernavn = brukernavn
        self._listeAvEmner = []
    
    def hentBrukernavn(self):
        return self._brukernavn
        