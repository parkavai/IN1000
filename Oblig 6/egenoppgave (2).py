""" Tok i bruk forslaget for egenoppgaven hvor man skal lage et objekt som består
av hobbyene til en person. Videre lager jeg klassen utifra oppgavebeskrivelsen
med en konstruktør hvor vi skal ha en tom liste, en metode som legger til
hobbyer i en liste og en metode som skriver ut navn og alder henter ut metoden
som skriver ut listen av hobbyer """

class Person:
    def __init__(self):
        self._hobbyer = []

    def leggTilHobby(self,tekststreng):
        self._hobbyer.append(tekststreng)

    def skrivHobbyer(self):
        return self._hobbyer

    def skrivUt(self,navn,alder):
        print("Oversikt over hobbyene til :", navn, alder)
        return self.skrivHobbyer()
