import sys
min_val = 0
correct = False
compQ = ""

max_val = 0
print(max_val)
max_val = int(sys.argv[1])

if len(sys.argv) < 1:
 max_val = int(input("Please enter a high number: "))

num = int(input(f"Please enter a number between 1 and {max_val}: "))


while correct == False:
    guess = (max_val + min_val)//2
    compQ = input(f'is this your number? {guess} enter "h" for too high "l" for too low or "y" for yes: ')
    if compQ == 'y':
        print("Looks like I got the number correct")
        correct = True
    elif compQ == 'h':
        max_val = guess
    elif compQ == 'l':
        min_val = guess
    else:
        print("Please enter a valid option!")