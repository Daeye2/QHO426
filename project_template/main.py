"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

import process
import tui
import visual

def main_function():
    # Display the title
    title = "DisneyLand Review Analyser"
    dashes = "-" * len(title)  # Print dashes equal to the length of the title

    print(dashes)  # Print dashes above the title
    print(title)   # Print the title
    print(dashes)  # Print dashes below the title

    # Try to load the dataset
    data = process.load_data("data/disneyland_reviews.csv")
    if not data:  # If data is empty, exit the program
        print("Failed to load the CSV. Exiting application.")
        return

    print(f"CSV loaded with {len(data)} entries.")

    while True:
        print("\nMain Menu:")
        print("[A] - View Data")
        print("[B] - View Visualizations")
        print("[C] - Export Data")
        print("Type 'exit' to close the application")
        select = input("Enter your choice: ").strip().upper()

        if select == 'A':
            handle_data_view(data)
        elif select == 'B':
            handle_visualization(data)
        elif select == 'C':
            handle_export(data)
        elif select.lower() == 'exit':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

def handle_data_view(data):
    # Handle the 'A' menu options
    select = tui.data_view_menu()
    if select == '1':
        park_name = input("Enter the park name: ")
        process.reviews_by_park(data, park_name)
    elif select == '2':
        park_name = input("Enter the park name: ")
        location = input("Enter the reviewer's location: ")
        count = process.reviews_by_location(data, park_name, location)
        print(f"{count} reviews found for {park_name} from {location}")
    elif select == '3':
        park_name = input("Enter the park name: ")
        year = input("Enter the year (YYYY): ")
        avg_rating = process.rating_by_year(data, park_name, year)
        print(f"Average rating for {park_name} in {year} is {avg_rating}")
    elif select == '4':
        process.score_by_location(data)

def handle_visualization(data):
    # Handle the 'B' menu options
    select = tui.visualization_menu()
    if select == '1':
        visual.pie_chart(data)
    elif select == '2':
        visual.bar_chart(data)
    elif select == '3':
        visual.scatter_chart(data)
    elif select == '4':
        park_name = input("Enter the park name: ")
        visual.top_locations(data, park_name)
    elif select == '5':
        park_name = input("Enter the park name: ")
        visual.monthly_average_rating(data, park_name)


def handle_export(data):
    format_choice = input("Enter export format (TXT, CSV, JSON): ").strip().upper()
    if format_choice in ["TXT", "CSV", "JSON"]:
        process.export_data(data, format_choice)
    else:
        print("Invalid format.")


if __name__ == "__main__":
    main_function()