"""
Task: Simple Calculator
Write a Python program that:

Prompts the user to enter two numbers.
Prompts the user to enter an operation (+, -, *, /).
Performs the specified operation on the two numbers.
Prints the result.
Requirements:
Use input() to get user input.
Use if-elif-else statements to handle different operations.
Handle division by zero with an appropriate message.
"""

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    if y ==0 and op == "/":
        print("Division by zero is not allowed")
    elif op == "+":
        print("The result is: ",x + y)
    elif op == "-":
        print("The result is: ", x - y)
    elif op == "*":
        print("The result is: ", x * y)
    elif op == "/" and y != 0:
        print("The result is: ", x / y)
        
        
main()