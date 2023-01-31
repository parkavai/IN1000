filtall = open("fil_tall.txt","r")

tallliste = []

def les_tall_fra_fil(fil):
    for linje in filtall:
        linje = linje.rstrip("\n")
        tallliste.append(int(linje))
    return tallliste

les_tall_fra_fil(filtall)

heltall = int(input("Skriv inn et heltall: "))

def antall_forekomster(liste,tall):
    teller = 0
    for i in liste:
        if tall == i:
            teller+=1
    return teller

print(antall_forekomster(tallliste,heltall))

def flest_forekomster(liste):
    verdi_med_flest_forekomster = liste[0]
    teller = antall_forekomster(liste, liste[0])

    for verdi in liste:
        if antall_forekomster(liste, verdi) > teller:
            verdi_med_flest_forekomster = verdi
            teller = antall_forekomster(liste, verdi)

    return verdi_med_flest_forekomster

def testprogram():
    mine_tall = les_tall_fra_fil(filtall)
    print ("Tallet 34 forekommer " + str(antall_forekomster(mine_tall, 34)) + " ganger")
    print ("Det er flest forekomster av tallet " + str(flest_forekomster(mine_tall)))

testprogram()
