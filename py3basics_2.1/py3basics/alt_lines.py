import sys


for filename in sys.argv[1:]:
    a = open("a.txt", "a")
    b = open("b.txt", "a")
    with open(filename, "r+") as f:
       ln = 0
       for l in f:
            print(f"{l} {ln}")
            if ln % 2 == 0:
                a.write(l)
            else:
                b.write(l)
            ln += 1
    a.close
    b.close