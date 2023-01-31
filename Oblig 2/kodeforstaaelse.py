# 1.) Er dette lovlig kode? Begrunn svaret.

""" Dette er ikke tillatt, og vi får feilmelding når programmet kjøres.
 Årsaken er, fordi det slås sammen et heltall og en tekststreng. """

# 2.) Hvilke problemer vil vi kunne møte på når vi kjører denne koden?

""" Det skrives en feilmelding i terminalen som skyldes av at vi slår
    sammen et heltall og en tekststreng. For å løse dette problemet, må
    variabel b konverteres til en string for at meldingen skal printes."""

a = input("Tast inn et heltall! ")
b = int(a)

if b < 10:
    print(str(b) + "Hei!")

# Slik ser den oppdaterte versjonen av oppgaven.
