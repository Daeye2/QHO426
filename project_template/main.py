"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
import csv
import process
import tui
import visual

def main():
    # Try to load the dataset
    data = process.load_data("disneyland_reviews.csv")
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
    return
def handle_visualization(data):
    return
def handle_export(data):
    return

if __name__ == "__main__":
    main()