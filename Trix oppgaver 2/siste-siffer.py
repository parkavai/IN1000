a = 43
b = 123
c = 324

if a % 10 == b % 10:
    print("a og b har like siste siffer")

if a % 10 == c % 10:
    print("a og c har like siste siffer")

if b % 10 == c % 10:
    print("b og c har like siste siffer")

""" For denne oppgaven så benyttets modulo for å se om det som er igjen i rest,
tilsvarer en siffer som er lik for to variabler. I dette tilfellet har vi a og
b hvor begge delt på 10, har en rest på tallet 3. 10*4=40 + 3, 10*12 + 3,
resten er altså 3 for å få de verdien nevnt ovenfor. """
