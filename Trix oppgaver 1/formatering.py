lengde = 10.101
bredde = 3.483

print(f'Rektangelet er {lengde} cm langt og {bredde} cm bredt. \n')

def beOmNavn(navneliste):
    print("Tast inn brukernavn \n")
    brukerInput = str(input("Navn: "))
    while True:
        for navn in navneliste :
            if brukerInput == navn:
                return navn
        brukerInput = str(input("Navn: "))
    

# beOmNavn(["Parka", "Kangey", "Rcsan"])

def dempDeg(tekst):
    if tekst == "":
        return ""
        
    lengde = len(tekst) - 1
    utropstegn = lengde
    while tekst[utropstegn - 1] == "!" and utropstegn != 0:
        utropstegn -= 1
        
    if utropstegn == 0:
        return "."
    
    tekst = tekst[0:utropstegn]
    tekst += "."
    return tekst

assert(dempDeg("abcde!!!")) == "abcde."
assert(dempDeg("!!")) == "."
assert(dempDeg("!abscde f!")) =="!abscde f."
assert(dempDeg("")) == ""

