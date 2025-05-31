# Task 1: Create a Dictionary of Student Marks

students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Ethan": 76
}

name = input("Enter the student's name: ").strip()

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print(f"Student '{name}' not found.")
