print("Start the program")

print("Enter a character:")

user_input = input()

if len(user_input) == 1:
    ascii_value = ord(user_input)
    print(f"The ASCII code for {user_input} is {ascii_value}.")
else:
    print("Error: Please enter exactly one character.")