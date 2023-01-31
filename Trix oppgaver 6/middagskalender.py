def lesInnMatFil(filnavn):
    matretter = []
    fil = open(filnavn, "r")

    for linje in fil:
        info = linje.split(",")
        matretter.append(info[0])

    return matretter

import random

def velgMatretter(n):
    matretter = lesInnMatFil("matretter.txt")
    valgt_mat = []

    for i in range(n):
        valgt_mat.append(random.choice(matretter))

    return valgt_mat

def skrivMatretterTilFil():
    fil = open("matplan.txt", "w")

    for mat in velgMatretter(3):
        fil.write(mat + "\n")
