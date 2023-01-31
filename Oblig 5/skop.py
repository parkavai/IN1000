""" Først defineres funksjonen "minfunksjon" som ikke har noen parametre.
Deretter defineres prosedyren "hovedprogram" som heller ikke har noen parametre.
Tilslutt kalles prosedyren "hovedprogram". Inne i "hovedprogram", opprettes variablene
"a" med verdi 42 og "b" med 0. Verdien til variabel "b", er 0 og denne verdien
blir derfor skrevet ut. Videre blir verdien til variabel "b", oppdatert til verdien i variabel "a"
som er 42. Deretter kaller vi på funksjonen "minfunksjon". I funksjonen har vi
en løkke hvor teller "x" iterer mellom verdiene 0 og 2. Vi har en variabel "c" som
tilsvarer verdien 2. I neste linje skrives ut verdien til variabel "c". Videre
blir verdien til variabel "c" oppdatert gjennom at verdien adderes med 1 som
er da 3. Deretter har vi variabel "b" med en verdi på 10. Denne skal så adderes
med verdien til variabel "a". Tilslutt returneres verdien til "b". I prosedyren
"hovedprogram", vil variabel "a" få tilordnet denne returverdien, dvs 10. Så skrives
ut verdiene til variabel "b" som er 42 og variabel "a" som er 10.

Men dette programmet vil krasje med en feilmelding i terminalen som nevner at
variabelen "a", ikke er definert i "minfunksjon" hverken "hovedprogram". Problemet
som oppstår er at variabelen "a" er ikke en global variabel, men en lokal variabel. Dermed vil
programmet krasje siden "minFunksjon" og "hovedprogram" er ikke i stand til å hente noe variabel
"a" i programmet. Om programmet gjør denne endringen, vil det ikke oppstå noe
feil og programmet vil fungere som vist under. """


a = 0

def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
        print(c)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

hovedprogram()
