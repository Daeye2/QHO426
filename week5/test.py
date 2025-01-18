def display_main_menu():
    print("Main Menu")
    print("[A] - View Data")
    print("[B] - View Visualizations")
    print("[C] - Export Data")
    print("Type 'exit' to close the application")
    return input("Enter your choice: ").strip().upper()

def display_data_view_menu():
    print("\nData View Menu")
    print("[1] - View all reviews for a specific park")
    print("[2] - Count reviews for a park from a location")
    print("[3] - Average rating for a park by year")
    print("[4] - Average score per park by location")
    return input("Enter your choice: ").strip()

def display_visualization_menu():
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