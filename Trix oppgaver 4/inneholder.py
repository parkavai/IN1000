def sammenLigne(settningEn, settningTo):
    returStreng = ""
    for char in settningEn:
        for char2 in settningTo:
            if char == char2:
                settningTo = settningTo.replace(char2, '', 1)
                returStreng += char
                break;
    return returStreng == settningEn

print(sammenLigne("Skol)e","S(kole"))
