"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

# main.py

import tui
import data_process
import visual


def main():
    # Load dataset and initialize application
    data = data_process.load_data("disneyland_reviews.csv")
    print(f"Dataset loaded with {len(data)} entries.")

    while True:
        # Display main menu and get user's choice
        choice = tui.display_main_menu()

        if choice == 'A':
            handle_data_view(data)
        elif choice == 'B':
            handle_visualization(data)
        elif choice == 'C':
            handle_export(data)
        elif choice.lower() == 'exit':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")


def handle_data_view(data):
    # Handle the 'A' menu options
    choice = tui.display_data_view_menu()
    if choice == '1':
        park_name = input("Enter the park name: ")
        data_process.display_reviews_by_park(data, park_name)
    elif choice == '2':
        park_name = input("Enter the park name: ")
        location = input("Enter the reviewer's location: ")
        count = data_process.count_reviews_by_location(data, park_name, location)
        print(f"{count} reviews found for {park_name} from {location}")
    elif choice == '3':
        park_name = input("Enter the park name: ")
        year = input("Enter the year (YYYY): ")
        avg_rating = data_process.average_rating_by_year(data, park_name, year)
        print(f"Average rating for {park_name} in {year} is {avg_rating}")
    elif choice == '4':
        data_process.average_score_by_location(data)


# def handle_visualization(data):
#     # Handle the 'B' menu options
#     choice = tui.display_visualization_menu()
#     if choice == '1':
#         visual.pie_chart_review_counts(data)
#     elif choice == '2':
#         visual.bar_chart_average_scores(data)
#     elif choice == '3':
#         park_name = input("Enter the park name: ")
#         visual.top_locations_by_rating(data, park_name)
#     elif choice == '4':
#         park_name = input("Enter the park name: ")
#         visual.monthly_avg_rating(data, park_name)
#
#
# def handle_export(data):
#     format_choice = input("Enter export format (TXT, CSV, JSON): ").strip().upper()
#     if format_choice in ["TXT", "CSV", "JSON"]:
#         data_process.export_data(data, format_choice)
#     else:
#         print("Invalid format.")


if __name__ == "__main__":
    main()
