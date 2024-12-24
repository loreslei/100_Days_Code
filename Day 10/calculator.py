def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

from logo_art import logo

print(logo[1], logo[0])

calculating = True

result = 0

repeat = ''

while calculating:
    if repeat == 'N' or repeat == '':
        number = int(input("What is the first number? "))
    elif repeat == 'END':
        calculating = False
        break
    else:
        number = result
              
    operator = input("What operation (+, -, *, /) would you like to perform on this number? ")
    second_number = int(input("What is the second number? "))
    
    if operator == '+':
        result = add(number, second_number)
    elif operator == '-':
        result = subtract(number, second_number)
    elif operator == '*':
        result = multiply(number, second_number)
    else:
        result = divide(number, second_number)
    
    print(f"{number} {operator} {second_number} = {result}")
    
    repeat = input(f"Type 'Y' to perform another calculation with this {result}.\nType 'N' to start a new calculation. Type 'END' to end the calculator program.\n").upper()
    
    