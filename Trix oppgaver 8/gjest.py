class Gjest:
    def __init__(self):
        self._underholdningsverdi = 0

    def underhold(self,heltall):
        self._underholdningsverdi += heltall

    def hentUnderholdningsverdi(self):
        return self._underholdningsverdi



class Rorbu():
    def __init__(self):
        self._gjester = []

    def nyGjest(self,gjest):
        for gjest in self._gjester:
            gjest.underhold(1)
        self._gjester.append(gjest)

    def fortellVits(self,heltall):
        for gjest in self._gjester:
            gjest.underhold(heltall)

    def antallGjester(self):
        antallGjester = 0
        for gjest in self._gjester:
            antallGjester = antallGjester + 1
        return antallGjester

    def hvorMorsomtHarViDet(self):
        underholdningsverdiTotal = 0

        for gjest in self._gjester:
            underholdningsverdiTotal = underholdningsverdiTotal + gjest.hentUnderholdningsverdi()
            underholdningsverdiSnitt = underholdningsverdiTotal/self.antallGjester()

            if(underholdningsverdiSnitt < 200):
                print("Kjedelig kveld")

            elif(underholdningsverdiSnitt < 400):
                print("Dette var jo litt gøy")

            elif(underholdningsverdiSnitt < 600):
                print("Dette var artig!")

            else:
                print("Dra på Lopphavet - bi dae godtar no så gyt e!")

rorbui = Rorbu()

knutleik = Gjest()
frisorenAnton = Gjest()
misko = Gjest()

rorbui.nyGjest(frisorenAnton)
rorbui.nyGjest(knutleik)
rorbui.nyGjest(misko)
rorbui.fortellVits(700)

rorbui.hvorMorsomtHarViDet()
