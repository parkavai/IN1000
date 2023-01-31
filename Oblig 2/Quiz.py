""" For denne oppgaven så har jeg laget en quiz som består av to spørsmål.
    Den ene er et mattespørsmål mens det andre er et geografisk spørsmål.
    Avhengig av hva bruker svarer så vil if/else betingelsene kjøre.
    For å løse oppgaven så må brukeren være bevisst på rekkefølgen av
    regneoperasjoner som f.eks: parentes,dele,gange,minus og pluss
    som vil gi dem svare 58."""

spoersmaal1 = int(input("Hva er (2+(8*7)): "))

svar1 = 58

# Etter å ha tastet inn svare, vil bruker få en beskjed om det var rett eller
# galt.

if spoersmaal1 == svar1:
    print("Det stemmer, (2+(8*7) tilsvarer 58!")

else:
    print(" Dette stemmer ikke, 2+(8*7) tilsvarer ikke " + str(spoersmaal1) + ", svaret er 58.")

# Andre spørsmål er et typisk geografisk spørsmål

spoersmaal2 = input("Hva er hovedstaten i Norge ")

# Skulle bruker skrive hovedstaten med liten forbokstav så har jeg gitt en
# melding som påminner dem med bruk av stor forbokstav foran egennavn til neste gang.

svar2 = "Oslo"

svar3 = "oslo"

if spoersmaal2 == svar2:
    print("Det stemmer, hovedstaten i Norge er Oslo!")

elif spoersmaal2 == svar3:
    print("Det stemmer, hovedstaten i Norge er Oslo, men husk storforbokstav foran egennavn!")

else:
    print(" Dette stemmer ikke, hovedstaten i Norge er ikke  " + spoersmaal2 + ", svaret er Oslo.")
