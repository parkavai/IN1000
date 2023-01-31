inp = input("Skriv inn en saldo: ")

inp2 = input("Skriv inn prisen for din vare: ")

saldo = float(inp)

vare = float(inp2)

if saldo >= vare:
    print("Du har råd til å kjøpe varen.")
else:
    print("Du har ikke råd til varen, du mangler", (vare-saldo), " kr.")
