# Task 2: Using the Math Module for Calculations

import math

try:
    user_input = input("Enter a number: ")
    number = float(user_input)

    if number > 0:
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine_value = math.sin(number)  # value in radians

        print("Square root of", number, "is:", square_root)
        print("Natural log (ln) of", number, "is:", natural_log)
        print("Sine of", number, "radians is:", sine_value)
    else:
        print("Please enter a number greater than 0.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
except Exception as e:
    print("An error occurred:", str(e))