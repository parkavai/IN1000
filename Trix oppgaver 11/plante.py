class Plante:
    def __init__(self,maksgrensevann):
        self._vannbeholder = 0
        self._maksgrensevann = maksgrensevann
        self._status = True

    def vannPlante(self,vannCl):
        self._vannbeholder = self._vannbeholder + vannCl
        if self._vannbeholder > self._maksgrensevann:
            self.levende = False
            print(self.levende)

    def nyDag(self):
        self._vannbeholder = self._vannbeholder - 20
        if self._vannbeholder < 0:
            self.levende = False
            print(self.levende)

    def levende(self):
        return self._status


greinar = Plante(40)
greinarTo = Plante(90)

greinar.vannPlante(10)
greinarTo.vannPlante(10)

greinar.nyDag()
greinarTo.nyDag()
greinar.nyDag()
greinarTo.nyDag()
