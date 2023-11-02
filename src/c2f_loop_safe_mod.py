import sys
import temp_conv as tc
i = ""
while True:

    i = input("Please enter a temp: ")
    if i.lower() == 'q':
        break

    try:
        c = int(i)
        f = tc.c2f(c)
    except ValueError:
        print("Must enter a valid number!")
        continue
    except:
        print("Something went wrong!")
        continue
    print(f'{c:.1f}c is {f:.1f}f')
