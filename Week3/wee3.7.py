# Prompt the user for a phrase
phrase = input("What phrase do you want to see in reverse? ")

# Use a for loop to display the phrase in reverse by iterating from the last character to the first
for index in range(len(phrase) - 1, -1, -1):
    print(phrase[index], end="")

print(f"\nPhrase: {phrase}")  # Move to a new line after the reversed phrase is displayed

