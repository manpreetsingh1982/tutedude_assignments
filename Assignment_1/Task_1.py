#Task 1: Perform Basic Mathematical Operations

#Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Perform basic mathematical operations on the above two numbers
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Validation: check divide by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "cannot divide by zero"

# Display the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)