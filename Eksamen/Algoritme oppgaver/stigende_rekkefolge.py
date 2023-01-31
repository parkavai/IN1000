def sjekk_stigende_rekkefolge(tallListe):
    if(len(tallListe) == 0):
        return False
    sisteindeks = len(tallListe) - 1
    for x in range(0,len(tallListe) - 1):
        if (tallListe[sisteindeks] < tallListe[x]):
            return False
        elif(sisteindeks == x):
            return True
    return True

assert(sjekk_stigende_rekkefolge([1,2,3,4,5,6,7])) == True
assert(sjekk_stigende_rekkefolge([1,2,3,4,2])) == False

