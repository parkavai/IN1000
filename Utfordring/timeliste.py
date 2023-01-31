def ordbok_timeliste(filnavn):
    fil = open(filnavn, "r")
    person = fil.readline().strip().split(",")
    ordbok = {}
    for p in person:
        ordbok[p] = []
    for linje in fil:
        linje = linje.strip().split(",")
        indeks = 0
        while indeks != len(linje):
            ordbok[person[indeks]].append(int(linje[indeks]))
            indeks += 1
    return ordbok 

timeliste1 = ordbok_timeliste("timelister1.txt")

timeliste2 = ordbok_timeliste("timelister2.txt")

def slaa_sammen(ordbok1, ordbok2):
    ferdig_ordbok = ordbok1 
    for nokkel in ordbok2:
        indeks = 0
        if(nokkel in ferdig_ordbok):
            while (indeks < len(ordbok2[nokkel])):
                ferdig_ordbok[nokkel][indeks] += ordbok2[nokkel][indeks]
                indeks += 1
        else:
            ferdig_ordbok[nokkel] = ordbok2[nokkel]
    return ferdig_ordbok

print(slaa_sammen(timeliste1,timeliste2))
