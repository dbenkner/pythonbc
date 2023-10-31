user_input = ""
while user_input != "q":
    user_input = input('Please enter a simple math problem to solve: ')
    if user_input.lower() == "q":
        break
    user_split = user_input.split()

    a = int(user_split[0])
    opp = user_split[1]
    b = int(user_split[2])



    def add(a, b):
        return a + b
    def sub(a,b):
        return a - b
    def div(a,b):
        if (b == 0):
            print ('Cannot divide by 0!')
            return 
        return a/b
    def mul(a,b):
        return a * b

    if opp == "+":
        print(add(a,b))
    elif opp == "-":
        print(sub(a,b))
    elif opp == "*":
        print(mul(a,b))
    elif opp == "/":
        print(div(a,b))
    else:
        print("PLease enter a valid operation!")
