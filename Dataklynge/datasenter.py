## Samlet offentlige grensnitt for klassene til prosjektoppgave i IN1000, høst 2021
#
# * Denne teksten fjernes og klassene fordeles på filer før implementasjon*
# Grensesnittet er dokumentert i samme standard format som læreboken benytter.
# Det finnes mange alternative formater og verktøy for dokumentasjon av
# programmer, og en arbeidsplass eller kunde vil gjerne ha en standard man
# må tilpasse seg.
# Merk at informasjonen som er oppgitt her tilsvarer klassenes *offentlige
# grensesnitt* (public interface) - den informasjonen brukerne av klassen har
# behov for. Du bestemmer *implementasjonen* - og vil kunne endre den i
# ettertiden uten at programmer som bruker klassene påvirkes.


## Klasse for representasjon av et datasenter
#
class Datasenter:

    ## Oppretter et datasenter
    #
    def __init__(self):
        self._regneklyngeordbok = {}

    ## Leser inn data om en regneklynge fra fil og legger
    # den til i ordboken
    # @param filnavn filene der dataene for regneklyngen ligger
    def lesInnRegneklynge(self, filnavn):
        fil = open(filnavn, "r")
        filSplit = filnavn.split(".")
        antNoderPerRack = int(fil.readline())
        regneklynge = Regneklynge(antNoderPerRack)
        for linje in fil:
            alledata = linje.strip().split()
            antNoder = int(alledata[0])
            minnePerNode = int(alledata[1])
            antProsessorPerNode = int(alledata[2])
            rack = Rack()
            regneklynge._rackliste.append(rack)
            i = 0
            while i != antNoder:
                node = Node(minnePerNode, antProsessorPerNode)
                if regneklynge.settInnNode(node) == False:
                    rack = Rack()
                    rack.settInn(node)
                    regneklynge._rackliste.append(rack)
                i += 1
        self._regneklyngeordbok[filSplit[0]] = regneklynge
                

    ## Skriver ut informasjon om alle regneklyngene
    #
    def skrivUtAlleRegneklynger(self):
        for nokkel in self._regneklyngeordbok.keys():
            regneklynge = self._regneklyngeordbok[nokkel]
            print(f"Informasjon om regneklyngen {nokkel} \n")
            print(f"Antall rack: {regneklynge.antRacks()} \n")
            print(f"Antall noder: {regneklynge.noderMedNokMinne(1024)} \n")
            print(f"Antall prosessorer: {regneklynge.antProsessorer()} \n")

    ## Skriver ut informasjon om en spesifikk regeklynge
    # @param navn navnet på regnekyngen
    def skrivUtRegneklynge(self, navn):
        regneklynge = self._regneklyngeordbok[navn]
        print(f"Informasjon om regneklyngen {navn} \n")
        print(f"Antall rack: {regneklynge.antRacks()} \n")
        print(f"Antall noder: {regneklynge.noderMedNokMinne(64)} \n")
        print(f"Antall prosessorer: {regneklynge.antProsessorer()} \n")

## Klasse for representasjon av regneklynge i et datasenter.
#
class Regneklynge:
    ## Oppretter en regneklynge og setter maks antall
    # det er plass til i et rack
    # @param noderPerRack max antall noder per rack
    def __init__(self, noderPerRack):
        self._rackliste = []
        self._noderPerRack = noderPerRack

    ## Plasserer en node inn i et rack med ledig plass, eller i et nytt
    # @param node referanse til noden som skal settes inn i datastrukturen
    def settInnNode(self, node):
        for rack in self._rackliste:
            if(rack.getAntNoder() < self._noderPerRack):
                rack.settInn(node)
                return True
        return False
            

    ## Beregner totalt antall prosessorer i hele regneklyngen
    # @return totalt antall prosessorer
    def antProsessorer(self):
        antProsessorer = 0
        for rack in self._rackliste:
            antProsessorer += rack.antProsessorer()
        return antProsessorer

    ## Beregner antall noder i regneklyngen med minne over angitt grense
    # @param paakrevdMinne hvor mye minne skal noder som telles med ha
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        antNoder = 0
        for rack in self._rackliste:
            antNoder += rack.noderMedNokMinne(paakrevdMinne)
        return antNoder

    ## Henter antall racks i regneklyngen
    # @return antall racks
    def antRacks(self):
        return len(self._rackliste)

## Klasse for representasjon av racks i en regneklynge.
#
class Rack:
    ## oppretter et rack der det senere kan plasseres noder
    #
    def __init__(self):
        self._nodeListe = []

    ## Plasserer en ny node inn i racket
    #  @param node noden som skal plasseres inn
    def settInn(self, node):
        self._nodeListe.append(node)

    ## Henter antall noder i racket
    # @return antall noder
    def getAntNoder(self):
        return len(self._nodeListe)

    ## Beregner sammenlagt antall prosessorer i nodene i et rack
    # @return antall prosessorer
    def antProsessorer(self):
        antProsessorer = 0
        for node in self._nodeListe:
            antProsessorer += node._antPros 
        return antProsessorer

    ## Beregner antall noder i racket med minne over gitt grense
    # @param paakrevdMinne antall GB minne som kreves
    # @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        antNoder = 0
        for node in self._nodeListe:
            if(node.nokMinne(paakrevdMinne) == True):
                antNoder += 1
        return antNoder


## Klasse for representasjon av noder i en regneklynge
#
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
        if(self._minne >= paakrevdMinne):
            return True 
        return False 