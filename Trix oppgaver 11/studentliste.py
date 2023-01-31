class Student:
    def __init__(self, navn, brukernavn, telefonnummer):
        self._navn = navn
        self._brukernavn = brukernavn
        self._telefonnummer = int(telefonnummer)

    def printInfo(self):
        print("Navn:", self._navn)
        print("Brukernavn:", self._brukernavn)
        print("telefonnummer:", self._telefonnummer)


def finnstudent(navn,ordliste):
    for i in ordliste:
        if ordliste[i]._navn == navn:
            return True
    return False


def testprogram():
    studentordbok = {}

    stud1 = Student("R", "S", 45131231)
    stud2 = Student("NONO", "LLL", 2313231)
    stud3 = Student("OO", "TRS", 6121311)

    studentordbok[stud1._navn] = stud1
    studentordbok[stud2._navn] = stud2
    studentordbok[stud3._navn] = stud3

    for i in studentordbok:
        print(studentordbok[i].printInfo())
        print("\n")

    print("Skriv navn til en student for å søke? Eller skriv stop for å avslutte")
    navn = input()
    while navn != "stop":
        if(finnstudent(navn, studentordbok)):
            print(navn + " er registrer")
        else:
            print(navn + " er ikke registrer")
        navn = input()

testprogram()
