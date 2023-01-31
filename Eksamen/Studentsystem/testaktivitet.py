from aktivitet import Aktivitet
from dato import Dato
from emne import Emne
from student import Student

emne = Emne("1050")
dag = Dato(2,9,21)
aktivitet = Aktivitet(emne, dag, "50")
aktivitet.registreroppmoete(Student("Karsten"))
aktivitet.registreroppmoete(Student("Ola"))
aktivitet.registreroppmoete(Student("Per"))
aktivitet.skrivUtOppmoeteStudenter()
print(aktivitet)



