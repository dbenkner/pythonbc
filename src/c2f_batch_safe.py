import sys
import logging
cstrs = sys.argv[1:]
logging.basicConfig(filename="c2f_batch.log", level=logging.DEBUG)

for cstr in cstrs:
    try:
        c = float(cstr)
    except ValueError:
        logging.error("Invalid number")
        print("MUST ENTER A NUMBER!")
        break
    f = (c * 9) / 5 + 32
    print(f"{c:.1f}c is {f:.1f}f")