def maks_temperatur_maaned(filnavn):
    fil = open(filnavn, "r")
    ordbok = {}
    for linje in fil:
        data = linje.strip().split(",")
        maaned = str(data[0])
        temperatur = float(data[1])
        ordbok[maaned] = temperatur
    return ordbok

def maks_temperatur_dag(maaned_ordbok, filnavn):
    fil = open(filnavn, "r")
    for linje in fil:
        data = linje.strip().split(",")
        maaned = str(data[0])
        temperatur = float(data[2])
        if(maaned_ordbok.get(maaned) < temperatur):
            print("Ny varmerekord for " + str(maaned) + " med " + str(temperatur))
            maaned_ordbok[maaned] = temperatur 
    return maaned_ordbok
    
maks_temperatur_dag(maks_temperatur_maaned("max_temperatures_per_month.csv"), "max_daily_temperature_2018.csv")

def varme_bolge(maaned_ordbok, filnavn):
    fil = open(filnavn, "r")
    temperatur_ordbok = {}
    dag_ordbok = {}
    for noekkel in maaned_ordbok:
        temperatur_ordbok[noekkel] = []
        dag_ordbok[noekkel] = []
    for linje in fil:
        data = linje.strip().split(",")
        maaned = str(data[0])
        dag = str(data[1])
        temperatur = float(data[2])
        temperatur_ordbok.get(maaned).append(temperatur)
        dag_ordbok.get(maaned).append(dag)
    for maaned in temperatur_ordbok:
        maaned_liste = temperatur_ordbok.get(maaned)
        dag_liste = dag_ordbok.get(maaned)
        indeks = 0
        while(indeks < len(maaned_liste)-4):
            temperatur = maaned_liste[indeks]
            sjekk = 0
            for x in maaned_liste[indeks:indeks+5]:
                if(x == temperatur):
                    sjekk += 1
            if(sjekk == 5):
                startdato = dag_liste[indeks]
                sluttdato = dag_liste[indeks+5]
                print("Varmebølge i maaned: " + maaned)
                print("Startdato: " + startdato)
                print("Sluttdato: " + sluttdato)
                print("Temperatur: " + str(temperatur))
            indeks += 1

varme_bolge(maks_temperatur_maaned("max_temperatures_per_month.csv"), "max_daily_temperature_2018.csv")
                


        
        


