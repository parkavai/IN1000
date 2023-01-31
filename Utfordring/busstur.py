def bussTur():
    sluttPunkt = 0
    antall = 0
    while sluttPunkt != 3:
        sluttPunkt +=1 
        stasjon = "Stasjon, " + str(sluttPunkt) + " Hvor mange gaar paa bussen?"
        print(stasjon)
        brukerInput = int(input())
        antall += brukerInput
        if(antall > 30):
            fots = antall - 30 
            print("Bussen er full. " + str(fots) + " maa gaa til fots!")
    
bussTur()
        
        
