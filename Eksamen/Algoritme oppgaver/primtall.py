""" Den første while-løkken vil gå så lenge teller ikke er mindre enn 1.
Dermed må vi sørge for at telleren synker med 1 for hver gang løkken kjører slik
at løkken ikke går uendelig. Vi har en if-setning som ser om primtallet ikke
returnerer noe i rest, for om den gjør det, blir "er_primtall" om til false, altså
tallet er ikke et primtall. Etter dette har vi en til if-setning som basert på
forrige if-sjekk, vil printe ut primtallet vårt. For hensikten med den første
if-setningen er å separere primtall og de som ikke er primtall. Derette skriver vi
ut kun de som er primtall. """


# A
inp = input("Gi heltall:")
tall = int(inp)

# B
def print_primtall(N):
    teller = N-1
    er_primtall = True

    while teller > 1 :
        if N % teller == 0 :
            er_primtall = False
        teller-=1

    if er_primtall :
        print("Fant primtall ", N)

while tall > 1 :
    print_primtall(tall)
    tall-=1
