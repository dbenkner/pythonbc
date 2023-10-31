import sys


for filename in sys.argv[1:]:
    with open(filename, "r+") as f:
       ln = 0
       for l in f:
            print(f"{l} {ln}")
            if ln % 2 == 0:
                a = open("a.txt", "a")
                a.write(l)
            else:
                b = open("b.txt", "a")
                b.write(l)
            ln += 1
