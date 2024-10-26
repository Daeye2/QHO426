# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Loop to get 3 numbers from the user
for i in range(1, 4):
    # Ask the user to enter a number
    num = int(input(f"Enter number {i}: "))

    # Check if the number is even or odd and increment the appropriate counter
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display the counts of even and odd numbers
print(f"Even numbers entered: {even_count}")
print(f"Odd numbers entered: {odd_count}")