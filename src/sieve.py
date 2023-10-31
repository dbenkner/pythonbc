count = 2
highest = 50
is_prime = []
numbers = range(2, highest +1)
for num in numbers:
    prime = True
    for num2 in range(2, num -1):
        if num % num2 == 0 and num != num2:
            prime = False
            break
    else: 
        is_prime.append(num)
    print(num, prime)
print(is_prime)