import math

inp = input("Skriv inn et desimaltall:  ")
radius = float(inp)

diameter = radius*2

areal = math.pi*radius*radius

omkrets = math.pi*diameter

print("Diameter: % 10.2f" % diameter)
print("Areal: % 11.2f" % areal)
print("Omkrets: % 10.2f" % omkrets)
