
def arverekke(forfader, etterkommer, forstefode): 
    barnebarn = forstefode.get(forfader)
    liste = []
    if(barnebarn != None):
        liste.append(forfader)
        liste.append(barnebarn)
    else:
        return []
    if(forstefode.get(barnebarn) == etterkommer):
        liste.append(forstefode.get(barnebarn))
        return liste
    else:
        return []

    
barn = {"Halfdan":"Harald", "Christian":"Hans", "Harald":"Eirik"}
personer = arverekke("Halfdan", "Eirik", barn)
print(personer)


    
