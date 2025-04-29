#Task 2: Create a Personalized Greeting

#Takes a user's first name and last name as input
fName = input("Enter your first name: ")

lName = input("Enter your second name: ")

if fName.strip() != "" and lName.strip() != "":
    fullName = fName + " " + lName
    print("Hello, " + fullName + "! Welcome to the Python program.")
else:
    print("Error: First name and Last name cannot be empty.")

