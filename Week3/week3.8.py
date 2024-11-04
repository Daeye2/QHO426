# Prompt the user for a phrase
phrase = input("What phrase do you want to see ? ")

# Use a for loop to display the phrase in reverse by iterating from the last character to the first
for index in range(len(phrase)):
    print(phrase[index])

print(f"Phrase: {phrase}")  # Move to a new line after the reversed phrase is displayed
