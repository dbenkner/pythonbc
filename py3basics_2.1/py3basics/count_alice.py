import sys

for filename in sys.argv[1:]:
    with open(filename, "r") as f:
        count = 0
        for l in f:
            if "Alice" in l:
                count += 1
        print(count)