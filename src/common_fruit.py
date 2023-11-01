with open("py3basics_2.1/py3basics/DATA/fruit1.txt") as f:
    fruits = f.read().splitlines()

fruits1 = set()
for fruit in fruits:
    fruits1.add(fruit)

with open("py3basics_2.1/py3basics/DATA/fruit2.txt") as f:
    furits = f.read().splitlines()
