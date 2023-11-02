
def mod(a,b):
    return a - (b * (a // b))

def percent(a,b):
    return a / b * 100

def exp(a,b):
    count = 1
    while count < b:
        a *= a
        count += 1
    return a

if __name__ == "__main__":
    print(10%2)
    print(mod(10,2))
    print(4%3)
    print(mod(4,3))
    print(percent(45,90))
    print(percent(96,35))
    print(exp(5,3))