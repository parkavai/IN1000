def samlet_vaksinasjon(krav_hvert_land):
    nyliste = set()
    for indreliste in krav_hvert_land:
        for vaksine in indreliste:
            nyliste.add(vaksine)
    return nyliste

print(samlet_vaksinasjon([["difteri", "tyfoidl", "hepatit", "difteri"]]))
