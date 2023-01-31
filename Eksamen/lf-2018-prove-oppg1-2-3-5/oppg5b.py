def gyldig(v):
    for start in range(len(v)):
        i = start
        teller = 0
        while v[i] != -1 and teller<len(v):
            teller +=1
            i = v[i]
            if i == start:
                return False
    return True

assert gyldig([2, -1, -1, 0])
assert not gyldig([1,-1, 3,4,2])
assert not gyldig([3, -1, -1, 4, 3])

def gyldig2(ansatte) :
    for i in range(len(ansatte)) :
        j = i
        sett = []
        while ansatte[j] != -1 :
            sett.append(j)
            j = ansatte[j]
            if j in sett :
                return False
    return True

assert gyldig2([2, -1, -1, 0])
assert not gyldig2([1,-1, 3,4,2])
assert not gyldig2([3, -1, -1, 4, 3])
