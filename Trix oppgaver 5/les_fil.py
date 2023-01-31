# Oppgave a)
fil = open("navn.txt")

# Oppgave b)
liste = []

# Oppgave c)
for linje in fil:
    liste.append(linje)

fil.close()

# Oppgave d)
print(liste)
