import matplotlib.pyplot as plt

def coordinate():
    """
    Prompts the user to enter x and y values and returns them as a tuple.
    """
    x = float(input("Enter an x value: "))
    y = float(input("Enter a y value: "))
    return x, y

def path():
    """
    Retrieves path coordinates from the user.
    Returns a list containing two lists: x_values and y_values.
    """
    print("Retrieving path...")
    x_values = []
    y_values = []

    for count in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return [x_values, y_values]

def run_task3():
    """
    Retrieves path data and plots a line plot using the provided coordinates.
    """
    values = path()

    plt.plot(values[0], values[1], 'r--o', label="Path")  # Red dashed line with circle markers
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Path Plot")
    plt.legend()
    plt.grid(True)
    plt.show()

run_task3()