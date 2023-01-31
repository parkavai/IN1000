class Temperatur:
    def __init__(self, celsius, streng):
        self._celsius = float(celsius)
        self._streng = streng

    def hent_Celsius(self):
        return self._celsius

    def hent_Kelvin(self):
        kelvin = self.hent_Celsius() + 273.15
        return kelvin

    def hent_Fahrenheit(self):
        fahrenheit = ((self.hent_Celsius()*9.5)+ 23)
        return fahrenheit

    def hent_String(self):
        if self._streng.lower() == "kelvin":
            print(self.hent_Kelvin())
        if self._streng.lower() == "celsius":
            print(self.hent_Celsius())
        if self._streng.lower() == "fahrenheit":
            print(self.hent_Fahrenheit())

def hovedprogram():
    bruker = input("Skriv inn enhet: ")
    temperatur = input("Skriv inn temperaturen: ")
    enhet = Temperatur(temperatur,bruker)
    enhet.hent_String()


hovedprogram()
hovedprogram()
hovedprogram()
