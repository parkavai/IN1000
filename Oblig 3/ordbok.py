# Oppgave 1.)

# Lager en ordbok med varene og prisen som tekststrenger.

varer = {"melk": "14,90", "brød": "24,90","yoghurt": "12,90","pizza": "39,90"}

# Skriver ut alle varene med hver sin pris.

print(varer)

# Lager to variabler for varene og to variabler for prisen til de varene.

vare1 = input("Skriv inn varenavn: ")

vare11 = input("Skriv inn pris for den første varen som du registrerte: ")

vare2 = input("Skriv inn et nytt varenavn: ")

vare22 = input("Skriv inn pris for den andre varen som ble registrert: ")

# Legger til varene i ordboken.

varer[vare1] = vare11
varer[vare2] = vare22

# Skriver ut den oppdaterte versjonen av ordboken.

print(varer)
