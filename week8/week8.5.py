import random
import matplotlib.pyplot as plt

def data():
    """
    Function to create a dictionary with user-defined line style, color, and marker style.
    """
    paths = {}

    # Ask user for line style
    line_style = input("What type of line would you like (:, --, or -)? ").strip()

    # Ask user for color
    color = input("What colour would you like (r, g, or b)? ").strip()

    # Ask user for marker style
    marker = input("What style of marker would you like (o, s, or ^)? ").strip()

    # Store values in the dictionary
    paths['line_style'] = line_style
    paths['color'] = color
    paths['marker'] = marker

    return paths

def generate():
    """
    Function to display line graphs based on user input.
    """
    print("How many lines would you like to display?")
    try:
        num_lines = int(input().strip())
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    for i in range(num_lines):
        print(f"\nConfiguring line {i + 1}:")
        values = data()

        # Generate random x and y values
        x = random.sample(range(1, 100), 10)  # 10 random x-values
        y = random.sample(range(1, 100), 10)  # 10 random y-values

        # Plot the graph using the user-defined values
        plt.plot(
            x, y,
            linestyle=values['line_style'],
            color=values['color'],
            marker=values['marker'],
            label=f'Line {i + 1}'
        )

    # Display the graph
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Graph')
    plt.show()

def run():
    """
    Function to run the program.
    """
    print("Running....")
    generate()
    print("Done!")

# Call the main function to run the program
if __name__ == "__main__":
    run()
