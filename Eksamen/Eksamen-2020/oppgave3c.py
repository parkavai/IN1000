def intTilString(tall,antallsiffer):
    strengTall = str(tall)
    lengde = len(str(tall))
    strengNull = ""
    antNull = antallsiffer - lengde
    if(lengde < antallsiffer):
        while(len(strengNull) < antNull):
            strengNull += "0"
    return strengNull+strengTall

assert intTilString(87, 4) == "0087"
assert intTilString(87, 2) == "87"
assert intTilString(87, 1) == "87"
assert intTilString(1, 11) == "00000000001"
assert intTilString(0, 2) == "00"
assert intTilString(0, 1) == "0"
        