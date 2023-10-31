import sys

cstrs = sys.argv[1:]

for cstr in cstrs:
    c = float(cstr)
    f = (c * 9) / 5 + 32
    print(f"{c:.1f}c is {f:.1f}f")