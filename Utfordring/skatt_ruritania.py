inntekt: float = float(input("Tast inn din inntekt: "))
begrensning = 10000
skatt: float = 0
if(inntekt < begrensning):
    skatt = inntekt * 0.10
    print("Du betaler, " + str(skatt) + " i skatt")
else:
    skatt = inntekt * 0.10
    resten = (inntekt-1000) * 0.30
    print("Du betaler, " + str(skatt) + " i skatt\n")
    print("imens resten av pengene betaler du, " + str(resten) + " i skatt\n")
