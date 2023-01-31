def liste_med_like_tall(tallListe):
    sjekk = tallListe[0]
    for tall in tallListe:
        if(sjekk != tall):
            return -1
    return sjekk