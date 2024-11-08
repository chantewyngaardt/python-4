# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apple", "pear", "banana", "orange"]

# TODO: Use a for loop to print each fruit in the list
for fruit in fruits:
    print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count > 0: 
    print(count)
    count -= 1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for n in range(1, 11):
    print(n**2)

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random

# TODO: Create a list of colors
colours = ["pink", "blue", "red", "green", "yellow"]

# TODO: Use a for loop to select and print 3 random colors from the list
for colour in range(3):
    print(random.choice(colours))

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations 

print(math_operations.add(7, 8))
print(math_operations.divide(9, 3))
print(math_operations.multiply(2, 6))
print(math_operations.subtract(10, 3))

# TODO: Use a while loop to create a simple calculator
def calculator():
    while True: 
        print("Enter '+' to add two numbers")
        print("Enter '-' to subtract two numbers")
        print("Enter '*' to multiply two numbers")
        print("Enter '/' to divide two numbers")

operation = input("Enter function here: ")
num1 = int(input("Enter a number here: "))
num2 = int(input("Enter another number here: "))

if operation == "+": 
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1*num2)
else: 
    print(num1/num2)

