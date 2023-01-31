from random import randint
from celle import Celle

class Spillebrett:

    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._generasjonsnummer = 0
        self._rutenett = []

        """ Lager den to-dimensjonale spillbrettet gjennom en nøstet for-løkke.
        For hver rad skal den legge til en liste og for hver kolonne skal den
        legge til et celle-objekt.
        """

        for r in range(0, self._rader):
            self._rutenett.append([])
            for k in range(0, self._kolonner):
                self._rutenett[r].append(Celle())

        # Kaller på metoden generer for at cellene skal få statusene sine.

        self._generer()

    def tegnBrett(self):
        print("\n"*10000)
        self.oppdatering()
        self._generasjonsnummer = self._generasjonsnummer + 1
        for rad in self._rutenett:
            for kolonne in rad:
                print(kolonne.hentStatusTegn(), end = "")
            print()


    def oppdatering(self):
        # Listene som skal endre statusen til cellen

        levendeceller = []
        doedeceller = []

        for r in range(0, self._rader):
            for k in range(0, self._kolonner):
                # Henter listen med alle nabocellene for en gitt celle
                sjekkenaboer = self.finnNabo(r,k)

                # Liste som skal fylles med alle levende naboceller
                levendenaboceller = []

                # En for-løkke som lar oss legge til nabocellene i "levendenaboceller"
                for i in sjekkenaboer:
                    if i.erLevende():
                        levendenaboceller.append(i)

                    """ Betingelsene som skal endre statusen til en celle på bakgrunn
                    om den er levende eller død og dets omgivelser. Først må vi sjekke
                    om en celle er levende. Hvis den er levende så må vi sjekke om
                    nabocellene vil påvirke statusen til den levende cellen. Dette
                    gjøres ved å referere til "levendenaboceller" hvor vi sjekker om
                    lengden til listen(altså antall naboer for den cellen), stemmer
                    overens med spillreglene. """

                if self._rutenett[r][k].erLevende():
                    if (len(levendenaboceller) == 2 or (len(levendenaboceller) == 3)):
                        levendeceller.append(self._rutenett[r][k])
                    else:
                        doedeceller.append(self._rutenett[r][k])

                    """ Hvis en celle ikke er levende, må vi se om den vil
                    reprodusere seg hvis nabocellene dets er 3. """

                else:
                    if (len(levendenaboceller) == 3):
                        levendeceller.append(self._rutenett[r][k])

        # Tilslutt endre statusen til cellene avhengig av hvilken liste de er i.

        for lc in levendeceller:
            lc.settLevende()

        for dc in doedeceller:
            dc.settDoed()

    def finnAntallLevende(self):
        teller = 0
        for rad in self._rutenett:
            for kolonne in rad:
                if kolonne.erLevende():
                    teller+=1
        return teller

    def _generer(self):
        for rad in self._rutenett:
            for kolonne in rad:
                random = randint(0,2)
                if random == 1:
                    kolonne.settLevende()

    def finnNabo(self, rad, kolonne):
        naboliste = []

        """ For å finne ut av naboene til en celle, må vi itere gjennom "rangen"
        som er oppgitt under. Årsaken er at vi ikke trenger å gå gjennom hele
        listen for å finne en celle sine naboer, men vi må spesifisere hvilken
        "range" vi må benytte for å finne en celle sine naboer. Dette gjøres gjennom
        (-1,2) siden "-1" vil ta for seg de nabocellene som er til venstre for
        cellen, "0" vil ta for seg de nabocellene som er i samme kolonne som cellen og
        "2" vil ta for seg de nabocellene som er til høyre for cellen.
        """

        for r in range(-1, 2):
            for k in range(-1, 2):

                """ Variablene "naborad" og "nabokolonne" er ment til å tilsvare
                de naboene som fins rundt den aktuelle cellen. "Naborad" vil tilsvare
                naboene som er over, under og i hjørnene til en celle. Imens
                "nabokolonne" vil tilsvare naboene som er til siden for en celle. """

                naborad = rad + r
                nabokolonne = kolonne + k

                gyldig = True

                # Sjekker om en nabocelle ikke er lik cellen som skal sjekkes.

                if (naborad == rad) and (nabokolonne == kolonne):
                    gyldig = False

                    """ Sjekker om en naborad ikke er utenfor brettet for å hindre
                    verdier som ikke er i brettet. I tillegg til om naboraden ikke
                    er større enn den aktuelle raden for de nabocellene er ikke nødvendig. """

                if (naborad < 0) or (naborad >= self._rader):
                    gyldig = False

                    """ Sjekker om en nabokolonne ikke er utenfor brettet for å hindre
                    verdier som ikke er i brettet. I tillegg til om nabokolonnen ikke
                    er større enn den aktuelle kolonnen for de nabocellene er ikke nødvendig. """

                if (nabokolonne < 0) or (nabokolonne >= self._kolonner):
                    gyldig = False

                    """ Legger til alle nabocellene i listen som er gyldige for den
                    cellen som ble referert til. """

                if gyldig:
                    naboliste.append(self._rutenett[naborad][nabokolonne])
        return naboliste
