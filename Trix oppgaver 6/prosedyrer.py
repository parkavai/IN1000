def skriv_med_trykk(tekststreng):
    print(tekststreng + "!")

i = 0
while i < 5:
    bruker = input("Gi meg et kraftuttrykk: ")
    skriv_med_trykk(bruker)
    i+=1
    if bruker == "nei":
        i = 5
