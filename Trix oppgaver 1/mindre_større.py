tall = int(input("Skriv inn et tall:\n "))

if tall < 10:
    print("Tallet er mindre enn 10 " )

elif tall == 10 or tall == 20:
    print("Tallet tilsvarer: " + str(tall))

elif tall > 10 and tall < 20:
    print("Tallet er større enn 10 ")

else:
    print("Tallet er større enn 20 ")
