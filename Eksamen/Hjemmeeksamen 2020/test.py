Ordbok = []

synonymer = [["a", "e", "o"], ["k", "l", "p"]];

def lagSynonymOrdbok(synonymer):
    for x in synonymer:
        nyliste = []
        for y in x:
            for z in y:
                if(y != z):
                    nyliste.append(y)
        Ordbok[y].append(nyliste);



lagSynonymOrdbok(synonymer)
for verdi in Ordbok:
    print(verdi)
