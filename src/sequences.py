ctemps = [-40, 0, 37, 75, 100]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

for c in ctemps: 
    f = ((9 * c) / 5) + 32
    print(f"The tempature in celcius is {c:.1f}c and in ferehainhite is {f:.1f}")

clean_fruits = [fruit.lower().strip() for fruit in fruits]

print(clean_fruits)