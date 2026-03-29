import sys 
import os 
def add(num1, num2):
    add = num1 + num2 
    return add 

def sub(num1, num2):
    sub = num1 - num2 
    return sub 

def mul(num1, num2):
    mul = num1 * num2 
    return mul 

def div(num1, num2):
    if num2 == 0:
        return "Error: Division by Zero"
    return num1 / num2

# Ask user for input
num1 = int(input("Enter the first number: "))
operation = input("Enter operation (add, sub, mul, div): ")
num2 = int(input("Enter the second number: "))

if operation == "add":
    output = add(num1, num2)
elif operation == "sub":
    output = sub(num1, num2)
elif operation == "mul":
    output = mul(num1, num2)
elif operation == "div":
    output = div(num1, num2)
else: 
    output = "unknown operation"
print(output)

print(os.getenv("password"))
print(os.getenv("apitoken"))
print(os.getlogin)