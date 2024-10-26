print("enter the first number")
number1 = int(input())
print("enter the second number")
number2 = int(input())
print("enter the third number")
number3 = int(input())

even_no = 0
odd_no = 0


if number1 % 2 == 0:
    even_no = even_no + 1
else:
    odd_no = odd_no + 1

if number2 % 2 == 0:
    even_no = even_no + 1
else:
    odd_no = odd_no + 1

if number3 % 2 == 0:
    even_no = even_no + 1
else:
    odd_no = odd_no + 1

print(f"total numbers of even are {even_no} and the odd numbers are {odd_no}.")