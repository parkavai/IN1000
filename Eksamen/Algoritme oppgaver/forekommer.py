# Oppgave a

def forekommer(streng, bokstav):
    for x in range(len(streng)):
        if(streng[x] == bokstav):
            return True
    return False

# Oppgave b
def uten_repetisjon(tekst):
    nyStreng = ""
    for x in range(len(tekst)):
        if(tekst[x] not in str(nyStreng)):
            nyStreng += tekst[x]
    return nyStreng

""" 
ny_tekst = ""
    for i in range(len(tekst)):
        if not forekommer(tekst[0:i], tekst[i]):
            ny_tekst += tekst[i]
    return ny_tekst
"""

# Oppgave c
def antall_forskjellige(tekst):
    return len(uten_repetisjon(tekst))

# Tester
print(forekommer("inf1001", "i"))
print(uten_repetisjon("aababbabbac"))
print(antall_forskjellige("aababbabbac"))
