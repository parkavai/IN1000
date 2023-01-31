maaned = ["Januar","Februar", "Mars", "April", "Mai", "Juni", "July",
"August", "September", "Oktober", "November", "Desember"]

inp = input("Tast inn et tall: \n")
taste = int(inp)

if taste >= 0 and taste <= 11:
    print("Tallet som ble tastet inn tilsvarer følgende måned: ", maaned[taste])

else:
    print("Tast inn et gyldig tall")
