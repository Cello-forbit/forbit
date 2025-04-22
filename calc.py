# Simple calculator in Python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Input from the user
num1 = float(input("första numret: "))
num2 = float(input("andra numret: "))
operation = input("räknesätt (+, -, *, /): ")

if operation == '+':
    print(add(num1, num2))
elif operation == '-':
    print(subtract(num1, num2))
elif operation == '*':
    print(multiply(num1, num2))
elif operation == '/':
    print(divide(num1, num2))
else:
    print("Invalid input")