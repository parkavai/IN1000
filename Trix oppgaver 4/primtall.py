""" Hva ber oppgaven oss om å gjøre?
Oppgaven ber oss om å ta inn et tall fra brukeren.
Videre skal vi skrive ut alle primtallene før tallet bruker tastet inn.
"""

""" Hva bør vi ta hensyn til når vi skal løse oppgaven?

Hva er et primtall og hvordan utføres regnemetoden på python?
Et primtall er et tall som bare er delelig av seg selv og 1. Dvs, at resultatet
av divisjonen til et tall, ikke kan være 2. I Python så utføres regnemetoden
gjennom modulo-operator "%". Den utføres slik: tall % 2 != 0, slik kan vi få
skrevet ut alle tallene som er i rest som vil si alle primtallene.

Hvordan skal vi få skrevet alle primtallene før tallet bruker skriver inn?
Vi må ha en løkke som skriver ut alle primtallene før tallet bruker skriver inn.
Dvs, at vi må skrive ut alle primtallene under regnemetoden for å finne primtall,
som er da tall % 2 != 0. Derfor trenger vi en if-setning med dette som betingelse.

Da kan vi starte oppgaven.

"""

tast = int(input("Skriv inn tall: "))

for num in range(2,tast):
   for i in range(2,num):
       if (num % i) == 0:
           break
   else:
       print(num)
