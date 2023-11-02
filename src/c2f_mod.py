import sys
import temp_conv

c = int(input("Please enter a temp: "))


f = temp_conv.c2f(c)

print(f'{c:.1f}c is {f:.1f}f')