inp = input("Skriv inn din inntekt: ")

inntekt = float(inp)

skattegrense = 10000

if inntekt < skattegrense:
    skattebetaling = inntekt*0.1
    print("Så mye skatt må du betale " + str(skattebetaling))

elif inntekt >= skattegrense:
    skattebetaling = skattegrense*0.1
    inntekt = inntekt-skattebetaling
    skattebetaling2 = inntekt*0.3
    skatt = skattebetaling+skattebetaling2
    inntekt = inntekt-skatt
    print("Så mye inntekt har du igjen " + str(inntekt) + " etter å ha betalt " + str(skatt))


""" Løsningsforslag """

""" inp = input("Tast inn din inntekt:\n> ")
inntekt = float(inp)

if inntekt < 10000 :
    skatt = inntekt*0.1
else:
    skatt = 10000*0.1 + (inntekt - 10000)*0.3
print("Skatt:", skatt)"""
