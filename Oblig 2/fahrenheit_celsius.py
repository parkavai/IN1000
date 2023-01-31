# Oppgave 1.) Lager en variabel for temperatur som bruker må taste inn.

temperatur = int(input("Tast inn et temperatur: "))

# Oppgave 2.) Konverterer temperatur til fahrenheit.

fahrenheit = (temperatur)

# Oppgave 3.) Konverterer fahrenheit til celsius gjennom formelen.

celsius = ((fahrenheit) - 32) * 5/9

# Printer ut verdien for celsius. Sørget for at det skrives ut kun 2 desimaler
# framfor utallige mange desimaler. 

print("%0.2f" % celsius)
