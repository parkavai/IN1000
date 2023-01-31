class Student:
    def __init__(self, navn, score, quiz):
        self._navn = navn
        self._score = score
        self._quiz = quiz
        self._gjennomsnitt = 0

    def leggTilQuizScore(self,nyscore):
        self._score += nyscore
        self._quiz += 1

    def gjennomsnittligScore(self):
        self._gjennomsnitt = self._score/self._quiz
        return self._gjennomsnitt

    def skrivUt(self):
        print(self._navn, self._score, self._quiz, self._gjennomsnitt)

# Oppgave e:
joakim = Student("Joakim", 0, 0)
kristin = Student("Kristin", 100, 1)
dag = Student("Dag", 50, 1)

# Oppgave f:
joakim.leggTilQuizScore(60)
joakim.leggTilQuizScore(45)

kristin.leggTilQuizScore(95)
kristin.leggTilQuizScore(47)

dag.leggTilQuizScore(3)
dag.leggTilQuizScore(2)

# Oppgave g
joakim.skrivUt()
print("Gjennomsnittlig score:", joakim.gjennomsnittligScore())
kristin.skrivUt()
print("Gjennomsnittlig score:", kristin.gjennomsnittligScore())
dag.skrivUt()
print("Gjennomsnittlig score:", dag.gjennomsnittligScore())
