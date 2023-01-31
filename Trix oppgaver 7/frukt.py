class Frukt:
    def __init__(self, navn, vann, spiselig):
        self._navn = navn
        self._vann = vann
        self._spiselig = spiselig

    def hentNavn(self):
        return self._navn

    def hentVann(self):
        return self._vann

    def erSpiselig(self):
        if self._spiselig == True:
            return True
        else:
            return False

    def skrivUt(self):
        print(self._navn, self._score, self._quiz, self._gjennomsnitt)


groentEple = Frukt("Grønt Eple", 86, True)
roedtEple = Frukt("Rødt Eple", 89, True)
hasselNoett = Frukt("Hasselnøtt", 12, True)
sukkerert = Frukt("Sukkerert", 89, True)
trollhegg = Frukt("Trollhegg", 90, False)

fruktliste = [groentEple,roedtEple,hasselNoett,sukkerert,trollhegg]

spiseligevannfrukter = []

for i in fruktliste:
    if ((i.erSpiselig()) and (i.hentVann() > 85)):
        spiseligevannfrukter.append(i)

print("Spiselige Vannfrukter:")
for enFrukt in spiseligevannfrukter:
    print(enFrukt.hentNavn())
