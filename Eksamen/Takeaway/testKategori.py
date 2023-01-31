from kategori import Kategori
from rett import Rett

rett1 = Rett("Pizza", 55 ,["ost", "broed"])
rett2 = Rett("Pasta", 100, ["jern", "ost"])

test = Kategori("Middag",[rett1,rett2])
print(test.hentOkRetter(["ost", "jern"]))

