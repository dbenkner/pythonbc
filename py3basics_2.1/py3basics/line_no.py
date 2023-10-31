import sys


for filename in sys.argv[1:]:
    with open(filename, "r") as f:
        print(list(enumerate(f)))