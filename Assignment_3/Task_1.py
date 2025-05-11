# Task 1: Calculate Factorial Using a Function

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


try:
    user_input = input("Enter a number: ")

    if user_input.strip().isdigit():
        num = int(user_input)

        print("Factorial of", num, "is:", factorial(num))
    else:
        print("Invalid input. Please enter a non-negative integer.")
except Exception as e:
    print("An error occurred:", str(e))