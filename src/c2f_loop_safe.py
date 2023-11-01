import sys

i = ""
while True:

    i = input("Please enter a temp: ")
    if i.lower() == 'q':
        break

    try:
        c = int(i)
        f = ((9 * c) / 5) + 32
    except ValueError:
        print("Must enter a valid number!")
        continue
    except:
        print("Something went wrong!")
        continue
    print(f'{c:.1f}c is {f:.1f}f')
