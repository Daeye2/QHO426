
print("Program Started!")

# Prompt the user to enter a single character
print("Please enter a standard character:")

# Read user input
user_input = input()

# Check if the length of the input is 1
if len(user_input) == 1:
    # Calculate the ASCII code using ord()
    ascii_code = ord(user_input)
    # Display the ASCII code result
    print(f"The ASCII code for {user_input} is {ascii_code}.")
else:
    # Display an error message if input is not a single character
    print("Error: Please enter exactly one character.")

# End the program with a message
print("Program Ended!")
