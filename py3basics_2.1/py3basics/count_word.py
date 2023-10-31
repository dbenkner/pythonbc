import sys

search = sys.argv[1]
for filename in sys.argv[2:]:
    with open(filename, "r") as f:
        count = 0
        for l in f:
            if search.lower() in l.lower():
                count += 1
        print(f"{filename} {count}")