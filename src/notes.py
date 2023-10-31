fruits = ['watermelon', 'apple', 'apricot', 'grapes', 'blueberries']

ufruits = [fruit.upper() for fruit in fruits]
afruits = [fruit.title() for fruit in fruits if fruit.startswith('a')]

print("ufruits:", ufruits)
print("afruits:", afruits)

gufruits = (fruit.upper() for fruit in fruits)
gafruits = (fruit.title() for fruit in fruits)

fruits = ['grapes']

print("gufruits:", ufruits)
print("gafruits:", afruits)

with open("example.txt", "r+") as fileobject:
    print("test")

airports = {'IAD' : 'Dulles', 'SEA': 'Seattle-Tacoma'}

for abbr, airport in airports(items())