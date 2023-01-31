class Node:

    def __init__(self, minne, prosessorer):
        self._minne = minne
        self._antPros = prosessorer

    def antProsessorer(self):
        return self._antPros

    def nokMinne(self,paakrevdMinne):
        return self._minne >= paakrevdMinne


class Rack:

    def __init__(self):
        self._listeAvNoder = []

    def settinn(self, node):
        self._listeAvNoder.append(node)

    def getAntNoder(self):
        return len(self._listeAvNoder)

    def antProsessorer(self):
        alleprosessorer = 0
        for noder in self._listeAvNoder:
            alleprosessorer += noder.antProsessorer()
        return alleprosessorer

    def noderMedNokMinne(self,paakrevdMinne):
        antallnoder = 0
        for noder in self._listeAvNoder:
            if noder.nokMinne(paakrevdMinne):
                antallnoder += 1
        return antallnoder

class Regneklynge:

    def __init__(self, noderPerRack):
        self._noderPerRack = noderPerRack
        self._listeAvRack = []

    def settInnNode(self,node):
        ledigRack = None
        i = 0
        while ledigRack == None and i < len(self._listeAvRack):
            if self._listeAvRack[i].getAntNoder() < self._noderPerRack:
                ledigRack = self._listeAvRack[i]
            i +=1
        if ledigRack == None:
            ledigRack = Rack()
            self._listeAvRack.append(ledigRack)
        ledigRack.settinn(node)
        """
        for rack in self._listeAvRack:
            if rack.getAntNoder() < self._noderPerRack:
                rack.settinn(node)
            elif rack.getAntNoder() > self._noderPerRack:
                nyRack = Rack()
                self._listeAvRack.append(Rack)
        """

    def antProsessorer(self):
        antallprosessorer = 0
        for rack in self._listeAvRack:
            antallprosessorer += rack.antProsessorer()
        return antallprosessorer

    def noderMedNokMinne(self,paakrevdMinne):
        for rack in self._listeAvRack:
            if rack.noderMedNokMinne(paakrevdMinne):
                return rack.getAntNoder()

    def antRacks(self):
        len(self._listeAvRack)

class Datasenter:

	def __init__(self):
		self._regneklynger = {}

	def lesInnRegneklynge(self, filnavn):
		fil = open(filnavn, "r")
		navn = filnavn.split(".")[0]
		noderPerRack = int(fil.readline().strip())
		regneklynge = Regneklynge(noderPerRack)
		self._regneklynger[navn] = regneklynge

		for linje in fil:
			data = linje.strip().split()
			for i in range(0, int(data[0])):
				node = Node(int(data[1]), int(data[2]))
				regneklynge.settInnNode(node)

		fil.close()

	def skrivUtAlleRegneklynger(self):
		for navn in self._regneklynger:
			self.skrivUtRegneklynge(navn)

	def skrivUtRegneklynge(self, navn):
		if navn in self._regneklynger:
			regneklynge = self._regneklynger[navn]
			print(navn, "har", regneklynge.antRacks(), "racks")
			print("Noder med minst 32GB:", regneklynge.noderMedNokMinne(32))
			print("Noder med minst 64GB:", regneklynge.noderMedNokMinne(64))
			print("Noder med minst 128GB:", regneklynge.noderMedNokMinne(128))
		else:
			print("Det finnes ingen regneklynge med dette navnet i datasenteret")

def hovedprogram():
    datasenter = Datasenter()
    datasenter.lesInnRegneklynge("abel.txt")
    datasenter.skrivUtAlleRegneklynger()

hovedprogram()
