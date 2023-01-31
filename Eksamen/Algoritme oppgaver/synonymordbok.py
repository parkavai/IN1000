def lag_synonymordbok(listeAvLister):
    ordbok = {}
    # Setter inn nøklene 
    for lister in listeAvLister:
        for element in lister:
            ordbok[str(element)] = []
    for lister in listeAvLister:
        for nokkel in lister:
            indeks = 0
            liste = []
            # Løkke som sørger for at vi kan iterere gjennom synonymene for den nøkkelen vi skal legge synonymene oppi
            while(indeks < len(lister)):
                # Sørger for at vi ikke legger til nøkkelen inn i lista
                if(nokkel != lister[indeks]):
                    liste.append(str(lister[indeks]))
                indeks +=1
            ordbok.get(nokkel).append(liste)
    return ordbok                

synonymer = [
                ["a", "e", "i", "o", "u"], \
                ["HOM", "c", "d"], \
                ["y", "HOM"], \
                ["k", "l","m", "n", "p", "q"], \
                ["x"]
            ]

synonymordbok = lag_synonymordbok(synonymer)

assert synonymordbok["e"] == [ ["a", "i", "o", "u"] ]
assert synonymordbok["a"] == [ ["e", "i", "o", "u"] ]
assert synonymordbok["u"] == [ ["a", "e", "i", "o"] ]
assert synonymordbok["c"] == [ ["HOM", "d"] ]
assert synonymordbok["HOM"] == [ ["c", "d"], ["y"]]
assert synonymordbok["x"] == [ [ ] ]