def fyllTilTi(tallene):
    while len(tallene)<10:
        tallene.append(0)
    return tallene

assert fyllTilTi([1,2,3]) == [1,2,3,0,0,0,0,0,0,0]
assert fyllTilTi([1,2,3,0,0,0,0,0,0,0]) == [1,2,3,0,0,0,0,0,0,0]

def fyllTilTi2(tallene):
    return tallene + [0]*(10-len(tallene))

assert fyllTilTi2([1,2,3]) == [1,2,3,0,0,0,0,0,0,0]
assert fyllTilTi2([1,2,3,0,0,0,0,0,0,0]) == [1,2,3,0,0,0,0,0,0,0]
