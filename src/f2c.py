import sys
import temp_conv as tc

f = int(input("Please enter a temp: "))

c = tc.f2c(f)

print(f'{f:.1f}f is {c:.1f}c')