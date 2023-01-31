def barnMedVoksen(alder1, alder2):
    return (alder1 >= 18 and alder2 < 18) or \
        (alder1 < 18 and alder2 >= 18)

assert barnMedVoksen(18,5)
assert barnMedVoksen(10,18)
assert not barnMedVoksen(18,30)
assert not barnMedVoksen(5,7)

def barnMedVoksen2(alder1, alder2):
    return (alder1-17.5) * (alder2-17.5) < 0

assert barnMedVoksen2(18,5)
assert barnMedVoksen2(10,18)
assert not barnMedVoksen2(18,30)
assert not barnMedVoksen2(5,7)
