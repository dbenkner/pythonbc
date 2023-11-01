a = open("a.txt", "a")
b = open("b.txt", "a")
aSort = []
bSort = []
with open("py3basics_2.1/py3basics/DATA/alt.txt", "+r") as f:
    ln = 0
    for l in f:
        if l.startswith('a'):
            aSort.append(l)
        if l.startswith('b'):
            bSort.append(l)
    aSort.sort(reverse = True)
    bSort.sort(reverse = True)
    for al in aSort:
        a.write(al)
    for bl in bSort:
        b.write(bl)
a.close
b.close