import sys

i = ""
while i == "":
    i = input("Please enter a temp: ")
    if i == 'q':
        break
    elif i == '':
        continue
    c = int(i)
    f = ((9 * c) / 5) + 32
    print(f'{c:.1f}c is {f:.1f}f')