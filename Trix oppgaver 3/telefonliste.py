min_telefonliste = {}

min_telefonliste = {"Arne": 22334455, "Lisa": 95959595, "Jonas": 97959795, "Peder": 12345678}

inp = input("Skriv inn et navn: ")

navn = inp

if navn in min_telefonliste:
    print(min_telefonliste[navn])

else:
    print("Vi har ikke lagret dette navnet. ")


""" Løsningsforslag

telefonbok = { "Arne": 22334455, "Lisa": 95959595, "Jonas": 97959795, "Peder": 12345678 }

navn = input("Skriv inn et navn: ")
if navn in telefonbok:
    nummer = telefonbok[navn], lager en variabel istedenfor å skrive nummeret rett inn.
    print("Telefonnummeret til", navn, "er", nummer)
else:
    print("Vi har ikke lagret telefonnummeret til", navn) """
