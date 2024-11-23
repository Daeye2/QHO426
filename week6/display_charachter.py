def display_chars(file_path, no_of_characters):
    with open(file_path) as file:
        data = file.read(no_of_characters)
        print(f"The first {no_of_characters} characters are:")
        print(data)


def run():
    display_chars("demo.txt.rtf", 10)


if __name__ == '__main__':
    run()