def temperatur_ordbok(filnavn):
    fil = open(filnavn, "r")
    linje = fil.split(",")
    ordbok = {}
    for data in linje:
        ordbok[str(data[0])] = float(data[1])
    return ordbok

def varmeste_temperaturer(ordbok, filnavn):
    fil = open(filnavn, "r")
    linje = fil.split(",")
    for data in linje:
        temp = ordbok[str(data[0])]
        if temp < float(data[2]): 
            ordbok[str(data[0])] = float(data[2])
    return ordbok 
