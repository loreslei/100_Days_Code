from logo_art import logo
def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():

    calculating = True

    answer = 0

    repeat = ''
    
    while calculating:
        if repeat == 'N' or repeat == '':
            num1 = float(input("Insert the first number: "))
        elif repeat == 'END':
            calculating = False
            break
        else:
            num1 = answer

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Insert the next number: "))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        repeat = input(f"Type 'Y' to perform another calculation with this {answer}.\nType 'N' to start a new calculation. Type 'END' to end the calculator program.\n").upper()
        
        




print(logo[1], logo[0])
calculator()