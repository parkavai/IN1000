prisListe = [
{"salat" : 12, "fisk" : 99, "melk" : 12, "brod" :12},
{"salat" : 22, "fisk" : 60, "melk" : 18, "brod" :21},
{"salat" : 8, "fisk" : 120, "melk" : 10, "brod" :19},
{"salat" : 18, "fisk" : 40, "melk" : 30, "brod" :59},
{"salat" : 15, "fisk" : 200, "melk" : 40, "brod" :9},
]

print(prisListe[0]["salat"])

salat = []
fisk = []
melk = []
brod = []

def finnbutikk(prisListe):
    for i in prisListe:
        print(str(i) + ": " + str(prisListe[i]) + " kr")

finnbutikk(prisListe)
