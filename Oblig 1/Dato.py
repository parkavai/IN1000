dag = input("Tast inn en dag: ")
maaned = input("Tast inn en måned: ")

dag2 = input("Tast inn en dag for den andre datoen: ")
maaned2 = input("Tast inn en måned for den andre datoen: ")

if(maaned < maaned2):
    print("Riktig rekkefølge")
elif(maaned2 < maaned):
    print("Feil rekkefølge")
else:
    if(dag < dag2):
        print("Riktig rekkefølge")
    elif(dag2 > dag):
        print("Feil rekkefølge")
    else:
        print("Samme dato!")
    