bruker = input("Skriv inn et brukernavn: ")

def velkommen(bruker):
    print(" Velkommen " + bruker)

velkommen(bruker)

def strenginator (s1, s2) :
    return s1 + " " + s2

strengA = "hei"
strengB = "verden!"

konkatenert = strenginator (strengA, strengB)
print(konkatenert)
