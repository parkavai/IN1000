from datasenter import Datasenter

def hovedprogram():
    dataSenter = Datasenter()

    dataSenter.lesInnRegneklynge("abel.txt")
    dataSenter.lesInnRegneklynge("saga.txt")

    dataSenter.skrivUtAlleRegneklynger()

hovedprogram()