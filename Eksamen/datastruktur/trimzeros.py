def trimZeros(a):
    forsteIndeks = 0
    while forsteIndeks < len(a) and a[forsteIndeks] == 0:
        forsteIndeks += 1
        sisteIndeks = len(a) - 1
    print(forsteIndeks)
    while sisteIndeks >= 0 and a[sisteIndeks] == 0:
        sisteIndeks -= 1
    print(sisteIndeks)
    return a[forsteIndeks:sisteIndeks + 1]

print(trimZeros([0,0,1,2,0,3,0,0,4,0]))
