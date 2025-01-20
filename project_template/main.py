"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
from fontTools.ttx import process


def main():
    # Try to load the dataset
    data = process.load_data("disneyland_reviews.csv")
    if not data:  # If data is empty, exit the program
        print("Failed to load the dataset. Exiting the application.")
        return

    print(f"Dataset loaded with {len(data)} entries.")

    while True:
        print("\nMain Menu:")
        print("[A] - View Data")
        print("[B] - View Visualizations")
        print("[C] - Export Data")
        print("Type 'exit' to close the application")
        choice = input("Enter your choice: ").strip().upper()

def handle_export(data):
    format_choice = input("Enter export format (TXT, CSV, JSON): ").strip().upper()
    if format_choice in ["TXT", "CSV", "JSON"]:
        data.export_data(data, format_choice)
    else:
        print("Invalid format.")


if __name__ == "__main__":
    main()
