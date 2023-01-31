class Datasenter:

	## Oppretter et datasenter
	#
	def __init__(self):
		self._regneklynger = {}

	## Leser inn data om en regneklynge fra fil og legger
	# den til i ordboken
	# @param filnavn filene der dataene for regneklyngen ligger
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

	## Skriver ut informasjon om alle regneklyngene
	#
	def skrivUtAlleRegneklynger(self):
		for navn in self._regneklynger:
			self.skrivUtRegneklynge(navn)

	## Skriver ut informasjon om en spesifikk regeklynge
	# @param navn navnet på regnekyngen
	def skrivUtRegneklynge(self, navn):
		if navn in self._regneklynger:
			regneklynge = self._regneklynger[navn]
			print(navn, "har", regneklynge.antRacks(), "racks")
			print("Noder med minst 32GB:", regneklynge.noderMedNokMinne(32))
			print("Noder med minst 64GB:", regneklynge.noderMedNokMinne(64))
			print("Noder med minst 128GB:", regneklynge.noderMedNokMinne(128))
		else:
			print("Det finnes ingen regneklynge med dette navnet i datasenteret")

class Regneklynge:
	## Oppretter en regneklynge og setter maks antall
	# det er plass til i et rack
	# @param noderPerRack max antall noder per rack
	def __init__(self, noderPerRack):
		self._racks = []

		if noderPerRack > 0:
			self._noderPerRack = noderPerRack
		else:
			self._noderPerRack = 1

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen
	def settInnNode(self, node):
		ledigRack = None
		i = 0

		while ledigRack == None and i < len(self._racks):
			if self._racks[i].getAntNoder() < self._noderPerRack:
				ledigRack = self._racks[i]
			i += 1

		if ledigRack == None:
			ledigRack = Rack()
			self._racks.append(ledigRack)

		ledigRack.settInn(node)

	## Beregner totalt antall prosessorer i hele regneklyngen
	# @return totalt antall prosessorer
	def antProsessorer(self):
		antPros = 0
		for rack in self._racks:
			antPros += rack.antProsessorer()
		return antPros

	## Beregner antall noder i regneklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		antNoder = 0
		for rack in self._racks:
			antNoder += rack.noderMedNokMinne(paakrevdMinne)
		return antNoder

	## Henter antall racks i regneklyngen
	# @return antall racks
	def antRacks(self):
		return len(self._racks)

class Rack:
	## oppretter et rack der det senere kan plasseres noder
	#
	def __init__(self):
		self._noder = []

	## Plasserer en ny node inn i racket
	#  @param node noden som skal plasseres inn
	def settInn(self, node):
		self._noder.append(node)

	## Henter antall noder i racket
	# @return antall noder
	def getAntNoder(self):
		return len(self._noder)

	## Beregner sammenlagt antall prosessorer i nodene i et rack
	# @return antall prosessorer
	def antProsessorer(self):
		antPros = 0
		for node in self._noder:
			antPros += node.antProsessorer()
		return antPros

	## Beregner antall noder i racket med minne over gitt grense
	# @param paakrevdMinne antall GB minne som kreves
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		antNoder = 0
		for node in self._noder:
			if node.nokMinne(paakrevdMinne):
				antNoder += 1
		return antNoder

class Node:
	## Oppretter en node med gitt minne-storrelse og antall prosessorer
	#  @param minne GB minne i den nye noden
	#  @param antPros antall prosessorer i den nye noden
	def __init__(self, minne, antPros):
		self._minne = minne
		self._antPros = antPros

	## Henter antall prosessorer i noden
	#  @return antall prosessorer i noden
	def antProsessorer(self):
		return self._antPros

	## Sjekker om noden har tilstrekkelig minne for et program
	#  @param paakrevdMinne GB minne som kreves for programmet
	#  @return True hvis noden har minst så mye minne
	def nokMinne(self, paakrevdMinne):
		return self._minne >= paakrevdMinne

def hovedprogram():
    datasenter = Datasenter()
    datasenter.lesInnRegneklynge("abel.txt")
    datasenter.skrivUtAlleRegneklynger()

hovedprogram()
