import week7
from week7 import tui, data_procces, visual
import csv

def main():
        # Try to load the dataset
        data = data_procces.load_data("disneyland_reviews.csv")
        if not data:  # If data is empty, exit the program
            print("Failed to load the dataset. Exiting the application.")
            return

        print(f"Dataset loaded with {len(data)} entries.")

        while True:
            print("\nMain Menu:")
            print("A - View Data")
            print("B - View Visualizations")
            print("C - Export Data")
            print("Type 'exit' to close the application")
            choice = input("Enter your choice: ").strip().upper()

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
        procces.display_reviews_by_park(data, park_name)
    elif choice == '2':
        park_name = input("Enter the park name: ")
        location = input("Enter the reviewer's location: ")
        count = data_procces.count_reviews_by_location(data, park_name, location)
        print(f"{count} reviews found for {park_name} from {location}")
    elif choice == '3':
        park_name = input("Enter the park name: ")
        year = input("Enter the year (YYYY): ")
        avg_rating = data_procces.average_rating_by_year(data, park_name, year)
        print(f"Average rating for {park_name} in {year} is {avg_rating}")
    elif choice == '4':
        data_procces.average_score_by_location(data)


def handle_visualization(data: object) -> object:
    # Handle the 'B' menu options
    choice = tui.display_visualization_menu()
    if choice == '1':
        week7.visual.pie_chart_review_counts(data)
    elif choice == '2':
        week7.visual.bar_chart_average_scores(data)
    elif choice == '3':
        park_name = input("Enter the park name: ")
        week7.visual.top_locations_by_rating(data, park_name)
    elif choice == '4':
        park_name = input("Enter the park name: ")
        week7.visual.monthly_avg_rating(data, park_name)


def handle_export(data):
    format_choice = input("Enter export format (TXT, CSV, JSON): ").strip().upper()
    if format_choice in ["TXT", "CSV", "JSON"]:
        data_procces.export_data(data, format_choice)
    else:
        print("Invalid format.")


if __name__ == "__main__":
    main()