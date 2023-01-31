def riktig_allePositive(tallene):
    #eneste forskjell er innrykk paa siste linje,
    #slik at siste return havner utenfor loekka
    for tall in tallene :
        if (tall < 0) :
            return False
    return True

assert riktig_allePositive([2,3])
assert not riktig_allePositive([-1,2,3])
assert not riktig_allePositive([2,3,-1])

#NB! Merk at en annen unoyaktighet er at oppgavebeskrivelsen
#henviser til positive tall, som matematisk sett ikke inkluderer tallet null
#Dette er ogsaa fint aa nevne, men kreves ikke for full uttelling

#Om man bare nevner aspektet med at null ikke er inkludert i positive tall,
#uten aa kommentere at koden oppforer seg annerledes enn intensjonen grunnet at Return True ligger i lokka,
#gir ogsaa dette uttelling, men ikke full.
