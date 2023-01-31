""" Prisene er som følger:
Brød: 20 kr.
Melk: 15 kr.
Ost: 40 kr.
Youghurt: 12 kr."""

broedtast = int(input("Skriv inn antall broed du vil ha: "))

broed = 20*broedtast

melktast = int(input("Skriv inn antall melk du vil ha: "))

melk = 15*melktast

osttast = int(input("Skriv inn antall ost du vil ha: "))

ost = 40*osttast

yoghurttast = int(input("Skriv inn antall yoghurt du vil ha: "))

yoghurt = 12*yoghurttast

totalpris = broed+melk+ost+yoghurt

print("Hei, velokmmen til IFI-butikken! \n" )

print("Du skal betale: " + str(totalpris))

""" Løsningsforslag

pris_broed = 20
pris_melk = 15
pris_ost = 40
pris_youghurt = 12

sum = 0

print("Hei! Velkommen til IFI-butikken.")
inp = input("Hvor mange broed vil du ha?\n> ")
sum+= int(inp)*pris_brød

inp = input("Hvor mange melk vil du ha?\n> ")
sum+= int(inp)*pris_melk

inp = input("Hvor mange ost vil du ha?\n> ")
sum+= int(inp)*pris_ost

inp = input("Hvor mange youghurt vil du ha?\n> ")
sum+= int(inp)*pris_youghurt

print("Du skal betale:", sum, "kr.")
"""
