personer = []
hunder = []

fil = open("navn.txt", "r")
for linje in fil :
    if linje[0] == "H":
        hunder.append(linje[2:-1])
    elif linje[0] == "P":
        personer.append(linje[2:-1])
    else:
        print("Feil i linjeformat:\n", linje)

fil.close()

print("Personer")
print(personer)
print("\n\nHunder")
print(hunder)
