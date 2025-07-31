# Debug the Math Operations Program
# Program to perform basic math operations such as addition, subtraction, multiplication, and division.

import pyinputplus as pyip

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):

        if b == 0:
            return 'Error: Cannot divide by zero'
#        print("Error: Cannot divide by zero")
        else:
            return a / b
num1 = pyip.inputNum("Enter first number: ")
num2 = pyip.inputNum("Enter second number: ")
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result:", add(num1, num2))
elif operation == "-":
    print("Result:", subtract(num1, num2))
elif operation == "*":
    print("Result:", multiply(num1, num2))
elif operation == "/":
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation")
