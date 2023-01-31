synonymer = [
                ["a","e","i","o","u"], \
                ["HOM", "c", "d"], \
                ["y", "HOM"], \
                ["k","l","m","n","o","p","q"], \
                ["x"]
            ]

def lagsynonymordbok(ordbok):
    synonymordbok = {}
    for liste in ordbok:
        listeAvSynonymer = liste 
        for nokkel in liste:
            beholder = []
            if(nokkel not in synonymordbok):
                synonymordbok[nokkel] = []
            for ord in listeAvSynonymer:
                if(ord != nokkel):
                    beholder.append(ord)
            synonymordbok.get(nokkel).append(beholder)
    return synonymordbok
                


synonymordbok = lagsynonymordbok(synonymer)

assert synonymordbok["e"] == [ ["a","i","o","u"] ]
assert synonymordbok["a"] == [ ["e","i","o","u"] ]
assert synonymordbok["u"] == [ ["a","e","i","o"] ]
assert synonymordbok["c"] == [ ["HOM", "d"] ]
assert synonymordbok["HOM"] == [ ["c", "d"], ["y"] ]
assert synonymordbok["x"] == [ [] ]