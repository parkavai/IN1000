def ring(i, v):
    while v[i] != -1:
        i = v[i]
    return i

assert ring(1, [2, -1, -1, 0])==1
assert ring(3, [2, -1, -1, 0]) == 2
