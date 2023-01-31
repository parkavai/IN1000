def kalkulator(tall1, operasjon, tall2):
    tall1 = float(tall1)
    tall2 = float(tall2)
    operasjon = str(operasjon)
    verdi = {
        "/": tall1 / tall2,
        "*": tall1 * tall2,
        "+": tall1 + tall2,
        "-": tall1 - tall2
    }
    return verdi[operasjon]

print(kalkulator(4,"+",3))