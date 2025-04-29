# Task 1: Check if a Number is Even or Odd

input = input('Enter a number: ')

if input.strip().isdigit():
    num = int(input)
    if num % 2 == 0:
        print('Number is Even')
    else:
        print('Number is Odd')
else:
    print("Invalid input. Please enter a valid integer number.")