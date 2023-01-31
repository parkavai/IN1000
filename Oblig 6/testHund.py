from hund  import Hund

""" Utifra verdien metthet, skal vi retunere vekten til hunden. Dvs at en metode
vil returnere "none" siden vi ikke går inn i en if-betingelse. I dette tilfelle
vil de bli spring. """

def hovedprogram():
    hund1 = Hund(4, 5)

    print(hund1.spring())
    print(hund1.spring())
    print(hund1.spis(4))
    print(hund1.spis(4))

hovedprogram()
