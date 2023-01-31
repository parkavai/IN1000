class Node :
    def __init__ (self, verdi) :
        self._verdi = verdi
        self._neste = None

    def settInn (self, ny) :
        self._neste = ny

    # ...flere metoder vi ikke trenger..

    def skrivMeg (self) :
        print (self._verdi + "\n")
        if self._neste != None :
            self._neste.skrivMeg()


#3e
listeStart = Node("a")
ny = Node ("b")
listeStart.settInn(ny)
listeStart.skrivMeg()
print ("--------")

#3f
ny = Node ("c")
ny.settInn(listeStart)
listeStart = ny
listeStart.skrivMeg()
