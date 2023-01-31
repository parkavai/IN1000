""" For egenoppgaven så tok jeg utgangspunkt i forslaget om å lagre bursdag.
Jeg har lagd 2 tomme lister hvor den ene skal oppbevare informasjon om navnene
til vennene brukern taster inn. Den andre derimot består av bursdagene til de
vennene brukeren har angitt. Dette gjøres gjennom while-løkker, hvor hensikten
med de 2 første løkkene, er å lagre info som bruker taster inn. Jeg sørget for å
sette en grense på antall bursdager og venner som bruker kan taste inn.
Tilslutt skrives ut bursdagen til en venn gjennom den siste løkken. """


venner = []

bursdager = []

teller = 0
while teller < 7:
    venner_navn = input("Skriv inn navnet til vennen din: ")
    venner.append(venner_navn)
    teller+=1

print("")

teller = 0
while teller < 7:
    bursdag_dato = float(input("Skriv inn bursdagen til din venn: "))
    bursdager.append(bursdag_dato)
    teller+=1

print("")

print("Her ligger oversikten over bursdagene til dine venner. \n ")

skriveutbursdager = 0
while skriveutbursdager < 7:
    print("Bursdagen til: ",venner[skriveutbursdager] , " er ", str(bursdager[skriveutbursdager]))
    skriveutbursdager+=1
