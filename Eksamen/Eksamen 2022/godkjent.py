def godkjent(poenglista):
    i = 1
    sum = 0
    oppfylt = True 
    linje = ""
    for poeng in poenglista:
        sum += poeng
        if(i == 6):
            if(sum < 19):
                linje += "Ikke godkjent, poengsum: " + str(sum) + " er lavere enn 19 for de 6 første obligene /n"
                oppfylt = False 
        elif i == 7 or i == 8:
            if(poeng == 0):
                linje += "Ikke godkjent siden oblig " + str(i) + " har 0 /n"
                oppfylt = False 
        i += 1
    if(oppfylt == True):
        print("Obligkravet er oppfylt")
    else:
        print(linje)

print(godkjent([3,0,0,0,5,6,0,1]))