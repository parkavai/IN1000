# Oppgave a
def forekommer(tekst, tegn):
    for c in tekst:
        if c == tegn:
            return True
    return False

# Oppgave b
""" """
def uten_repetisjon(tekst):
    ny_tekst = ""
    for i in range(len(tekst)):
        if not forekommer(tekst[0:i], tekst[i]):
            ny_tekst += tekst[i]
    return ny_tekst

# Oppgave c
def antall_forskjellige(tekst):
    return len(uten_repetisjon(tekst))

# Tester
print(forekommer("inf1001", "i"))
print(uten_repetisjon("aababbabbac"))
print(antall_forskjellige("aababbabbac"))
