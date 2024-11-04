print("Please enter the sequence in form of 'X -- X'")

sequence = input()

print("Enter the character for the marker")
marker = input()
mposition1 = -1
mposition2 = -1

for position in range(0,len(sequence), 1 ):
    letter = sequence[position]

    if letter == marker:
        if (mposition1 == -1):
            mposition1 = position
    else:
        mposition2 = position

print(f"The distance between tow marker is {mposition2 - mposition1}")