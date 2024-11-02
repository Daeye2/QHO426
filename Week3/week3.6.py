# Prompt the user for a word
word = input("What word do you see? ")

# Use a for loop to display each character with its index position
for index, character in enumerate(word):
    print(f"Index {index}: {character}")

print("Done")