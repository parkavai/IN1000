# Oppgave 1.)

indeks = 0
tall = []
teller = 0
while teller<5:
    indeks = int(input("Skriv inn tall: "))
    tall.append(indeks)
    teller +=1
print(tall)

# Oppgave 2.)

teller = 0
sum = 0
while teller < len(tall):
    sum+=tall[teller]
    teller+=1
print("Sum av tallene i listen er: ", sum)

# Oppgave 3.)
teller = 0
print("Tall under 10:")
while teller < len(tall) :
    if tall[teller] < 10 :
        print(tall[teller])
    teller+=1

# Oppgave 4.)
finnes_fem = False
teller = 0
while teller < len(tall) :
    if tall[teller] == 5 :
        finnes_fem = True
    teller+=1
if finnes_fem :
    print("Fem finnes i listen")
else:
    print("Fem finnes ikke i listen")
