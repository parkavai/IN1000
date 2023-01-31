def sorter_timeliste(filnavn):
    fil = open(filnavn, "r")
    timelisteordbok = {}
    navn = fil.readline().strip().split(",")
    for linje in fil:
        timer = linje.strip().split(",")
        indeks = 0
        while(indeks < len(timer)):
            if(len(timelisteordbok) < len(navn)):
                timelisteordbok[navn[indeks]] = [int(timer[indeks])]
            else:
                timelisteordbok.get(navn[indeks]).append(int(timer[indeks]))
            indeks += 1
    return timelisteordbok

def slaa_sammen(timeliste1, timeliste2):
    for x in timeliste1:
        if(x in timeliste2):
            for timer in range(0, len(timeliste1.get(x))):
                    timeliste1.get(x)[timer] += timeliste2.get(x)[timer]
    return timeliste1
                    
print(slaa_sammen(sorter_timeliste("fil1.txt"), sorter_timeliste("fil2.txt")))

