# Prompt the user for the brightness level
brightness_level = int(input("What level of brightness is required? (Please enter an even number) "))

# Ensure the entered brightness level is even
if brightness_level % 2 != 0:
    print("Please enter an even number for the brightness level.")
else:
    # Generate a range of even numbers from 2 up to the brightness level
    for level in range(2, brightness_level + 1, 2):
        # Display the current brightness level using asterisks
        print("*" * level)

print("Brightness adjustment complete!")
