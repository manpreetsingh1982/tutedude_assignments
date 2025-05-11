# Task 2: Write and Append Data to a File

try:
    # Step 1: Write data
    data = input("Enter text to write to the file: ")

    file = open("..\content.txt", "w")
    file.write(data + "\n")
    file.close()
    print("Data successfully written to ontent.txt.")

    # Step 2: Append data
    more_data = input("Enter additional text to append: ")

    file = open("..\content.txt", "a")
    file.write(more_data + "\n")
    file.close()

    # Step 3: Read final content
    file = open("..\content.txt", "r")
    print("\nFinal content of content.txt:\n")
    for line in file:
        print(line.strip())

    file.close()
except Exception as e:
    print("An error occurred while working with the file:", str(e))