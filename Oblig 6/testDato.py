from dato import Dato

""" Her har vi en prosedyre sjekke om dagen i en bestemt måned, er 15 eller 1.
Vi trenger kun å legge til 15 eller 1, i sjekkeDato() da den metoden består av
if-sjekk fra tidligere. """

def hovedprogram():
    dato1 = Dato(15,2,2001)

    print(dato1.leseAvAar())

    print(dato1.stringDato())

    if dato1.sjekkeDato(15):
        print("Loenningsdag! ")
    elif dato1.sjekkeDato(1):
        print("Det er en ny måned, det betyr nye muligheter. ")
    else:
        return False

hovedprogram()
