def roter(matrise):
    returMatrise = []
    for i in range(0,len(matrise)):
        returMatrise.append([])
        for j in range(0, len(matrise[i])):
            returMatrise[i].append(matrise[j][i])
    return returMatrise
