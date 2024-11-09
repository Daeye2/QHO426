# Start the program with a message
print("Program Started!")

# Prompt the user to enter an ASCII code
print("Please enter an ASCII code:")

# Read user input and convert it to an absolute integer
try:
    user_input = int(input())
    ascii_code = abs(user_input)

    # Check if the number is in the range of printable characters (32 to 126 inclusive)
    if ascii_code in range(32, 127):
        # Get the ASCII character using chr()
        character = chr(ascii_code)
        # Display the result
        print(f"The character represented by the ASCII code {ascii_code} is '{character}'.")
    else:
        # Display an error message if the number is out of range
        print("Error: Please enter a number between 32 and 126 (inclusive) for printable ASCII characters.")
except ValueError:
    # Handle the error if the input is not a valid integer
    print("Error: Please enter a valid integer.")

# End the program with a message
print("Program Ended!")
