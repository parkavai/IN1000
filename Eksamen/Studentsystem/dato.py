class Dato:
    def __init__(self,dag, maaned, aar):
        self._dag = int(dag)
        self._maaned = int(maaned)
        self._aar = int(aar)
    
    def absoluttDato(self):
        dag = self._dag
        maaned = self._maaned
        aar = self._aar
        if(self._dag < 10):
            dag = "0" + str(self._dag)
        if(self._maaned < 10):
            maaned = "0" + str(self._maaned)
        if(self._aar < 10):
            aar = "0" + str(self._aar)
        return str(dag) + str(maaned) + str(aar)
    
    def __str__(self):
        linje = ""
        aar = "20" + str(self._aar)
        if(self._maaned == 9):
            linje += str(self._dag) + ". september " + aar
        elif(self._maaned == 10):
            linje += str(self._dag) + ". oktober " + aar
        elif(self._maaned == 11):
            linje += str(self._dag) + ". november " + aar
        elif(self._maaned == 12):
            linje += str(self._dag) + ". desember " + aar
        else:
            return "Aksepterer kun måneder mellom september og desember"
        return linje