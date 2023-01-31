""" Hos friske mennesker varierer kroppstemperaturen vanligvis
    mellom 36.5 og 37.5 grader. Lag et program som avgjør om en persons
    kroppstemperatur ligger henholdsvis under,innenfor eller over
    normal kroppstemperatur. Programmet skal lese kroppstemperaturen
    fra terminal. """

def sjekk(a):
    if a >= 36.5 and a <= 37.5:
        print("Kroppstemperaturen din er normal.")
    elif a < 36.5:
        print("Kroppstemperaturen ligger under 36.5 grader. ")
    else:
        print("Kroppstemperaturen din begynner å koke. ")

inp = input("Skriv inn din kroppstemperatur:\n")

kroppstemperatur = float(inp)

sjekk(kroppstemperatur)
