import csv


records = []
headings = []


def load_data(file_path):
    global records, headings
    print("Loading data...")

    with open(file_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        headings = next(csv_reader)

        for row in csv_reader:
            records.append(row)

def display_menu():
    print("""
      Please select one of the following options:
      [1] Display the names of all passengers
      [2] Display the number of passengers that survived
      [3] Display the number of passengers per gender
      [4] Display the number of passengers per age group
      
      Please select the option 1-4
         """)
    user_input = int(input())
    return user_input

def display_passengers():
    print("The names of the passengers are...")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)


def display_passenger_names():
    print("The names of the passengers are...")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)


def run():
    global records
    file_path = "titanic.csv"
    load_data(file_path)

    print(f"Successfully loaded {len(records)}")
    print("Done")

    selected_option = display_menu()

    print(f"You have selected {selected_option}")

    if selected_option == 1:
        display_passenger_names()
    else:
        print("Error! Option not recognised!")

run()
