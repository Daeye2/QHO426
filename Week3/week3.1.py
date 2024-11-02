print("How many numbers you want to add")

number = int(input())

sum_of_numbers = 0
total = 0

while sum_of_numbers < number:
    print(f"Please enter a number {sum_of_numbers + 1} of {number}")
    sum_number = int(input())
    total = total + sum_number
    sum_of_numbers = sum_of_numbers + 1

print(f"....Done! total of all number is {total}")
