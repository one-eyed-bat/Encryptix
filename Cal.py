

def calculate ():
    print("What would you like to calculate?")
    try:
        num_1 = int(input("Digit: "))
    except ValueError:
        print("Please choose a valid number")
        calculate()
    operand = input("Operand: ")
    if operand not in [ '+', '-', '*', '/']:
        print("Invalid choice. Please choose one of the following: +, -, *, or / ")
        calculate()

    try:    
        num_2 = int(input("Digit: "))
    except ValueError:
        print("please choose a valid number")
        calculate()

    if operand == '+':
        result = num_1 + num_2
    elif operand =='-':
        result = num_1 - num_2
    elif operand == '*':
        result = num_1 * num_2
    elif operand =='/':
        result = num_1 / num_2
    else:
        result = "invalid choice. Please choose +, -, *, or /."
    print(result)
    

   

calculate()
