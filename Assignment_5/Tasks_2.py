# Task 2: Demonstrate List Slicing

numbers = list(range(1, 11))  # [1, 2, 3, ..., 10]

extracted = numbers[:5]       # First five elements
reversed_list = extracted[::-1]  # Reversed version of the extracted list

print("Original list:", numbers)
print("Extracted first five elements:", extracted)
print("Reversed extracted list:", reversed_list)
