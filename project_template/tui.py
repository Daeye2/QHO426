"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def display_main_menu():
    #Displays the main menu .
    print("Main Menu")
    print("[A] - View Data")
    print("[B] - View Visualizations")
    print("[C] - Export Data")
    print("Type 'exit' to close the application")
    return input("Enter your choice: ").strip().upper()

def display_data_view_menu():
    # Displays the data view menu.
    print("\nData View Menu")
    print("[1] - View all reviews for a specific park")
    print("[2] - Count reviews for a park from a location")
    print("[3] - Average rating for a park by year")
    print("[4] - Average score per park by location")
    return input("Enter your choice: ").strip()

def display_visualization_menu():
    # Displays the visualization menu.
    print("\nVisualization Menu")
    print("[1] - Pie chart of review counts by park")
    print("[2] - Bar chart of average scores by park")
    print("[3] - Top 10 locations by rating for a park")
    print("[4] - Monthly average rating for a park")
    return input("Enter your choice: ").strip()


if __name__ == "__main__":
    display_main_menu()
    display_data_view_menu()
    display_visualization_menu()