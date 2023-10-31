min_val, max_val = 1, 26

compQ = ""
num = int(input("Please enter a number between 1 and 1000000: "))

while True:
    guess = (max_val + min_val)//2
    compQ = input(f'is this your number? {guess} enter "h" for too high "l" for too low or "y" for yes: ')
    if compQ == 'y':
        print("Looks like I got the number correct")
        break
    elif compQ == 'h':
        max_val = guess
    elif compQ == 'l':
        min_val = guess
    else:
        print("Please enter a valid option! (y)es, (h)igh, (l)ow!")