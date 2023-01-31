class Blaabaer:
    def __init__(self):
        self._vekt = 0.3

class Blaabaerplante:
    def __init__(self, stoerrelse):
        self._stoerrelse = stoerrelse
        self._baer = []

    def motta_vann(self):
        self._stoerrelse += 3

    def motta_gjoedsel(self):
        for i in range(5):
            self._baer.append(Blaabaer())

    def gi_baer(self):
        return self._baer.pop()


plante = Blaabaerplante(10)
plante.motta_vann()
plante.motta_gjoedsel()
plante.motta_gjoedsel()

baer = []
for i in range(3):
    baer.append(plante.gi_baer())

print("Stoerrelse: ", plante.stoerrelse)
print("Antal baer: ", len(plante.baer))
print("Plukket baer: ", baer)
