print("Please enter a the first  number")

number = int(input())

print("Please enter  the second  number")

number1 = int(input())

if number1 > number:
    print(f"The second number is {number1} is the biggest number")
elif number1 < number:
    print(f"The first number is {number} is the smallest number")
else:
    print("Both are equal")