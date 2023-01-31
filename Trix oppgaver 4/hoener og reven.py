print('Hvor mange hoener bor paa gaarden?')
antallHoener = int(input())

while(antallHoener > 0):



    print('kommer reven')
    kommerReven = input()
    kommerReven = kommerReven.lower()



    print('Sover bonden')
    soverBonden = input()
    soverBonden = soverBonden.lower()

    if(kommerReven == 'ja'):
        if(soverBonden == 'ja'):
            antallHoener = antallHoener - 1
            print('Det bor naa ' + str(antallHoener) + ' hoens i gaarden.\n')

        else:
            print('Det bor nå '+ str(antallHoener) + ' hoens i gaarden. Bonden selger ett reveskinn, og tjener 190kr\n')

    else:
        print('Alt er likt som dagen før\n')
