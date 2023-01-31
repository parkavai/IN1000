beholder = {}

betingelse = "ja"
while betingelse == "ja":
    groennsak = input("Skriv inn en grønnsak: ")
    pris = input("Skriv inn prisen for den grønnsaken: ")
    if pris.isdigit():
        beholder[groennsak] = pris
        betingelse = input("Vil du fortsette med å taste inn grønnsaker?")
    else:
        print("Ugyldig tall, prøv på nytt.")


for teller in beholder:
    print(beholder)
