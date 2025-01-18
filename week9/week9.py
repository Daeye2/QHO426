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
      [5] Display the number of survivors per age group"
      
      Please select the option 1-5
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


def display_num_survivors():
    # Count the number of survivors
    num_survived = sum(int(record[1]) for record in records)
    print(f"{num_survived} passengers survived")


def display_passengers_per_gender():
    females = 0
    males = 0
    for record in records:
        gender = record[4]  # Assuming column 4 is gender
        if gender == "male":
            males += 1
        elif gender == "female":
            females += 1
    print(f"females: {females}, males: {males}")


def display_passengers_per_age_group():
    # Count the number of passengers per age group
    children = 0
    adults = 0
    elderly = 0
    for record in records:
        age = record[5]
        if age:  # Check if age is not an empty string
            age = float(age)  # Convert age to a number
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")


def display_survivors_per_age_group():
    # Count the number of survivors per age group
    children = 0
    adults = 0
    elderly = 0
    for record in records:
        survived = int(record[1])  # Survival status
        age = record[5]
        if survived == 1 and age:  # Check if the passenger survived and age is not empty
            age = float(age)  # Convert age to a number
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1
    print(f"Survivors - children: {children}, adults: {adults}, elderly: {elderly}")


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
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised!")


run()
