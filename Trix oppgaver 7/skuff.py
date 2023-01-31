from sokk import Sokk

class Skuff():
    def __init__(self):
        self._minesokker = []

    def settInnSokk(self,sokk):
        self._minesokker.append(sokk)

    def sjekkStatus(self):
        antallhoyre = 0
        antallvenstre = 0
        for sokk in self._sokkeListe:
            if(sokk.hentSide().lower() == 'venstre'):
                antallVenstre = antallVenstre+1

            if(sokk.hentSide().lower() == 'hoyre'):
                antallHoyre = antallHoyre+1

        if(antallHoyre == antallVenstre):
            print('Alt i orden')
        else:
            print('Ulikt antall høyre- og venstresokker.')



sokkenLeif = Sokk("Venstre")
sokkenLuff = Sokk("Hoyre")
skuffen = Skuff()

skuffen.settInnSokk(sokkenLeif)
skuffen.sjekkStatus()
skuffen.settInnSokk(sokkenLuff)
skuffen.sjekkStatus()
