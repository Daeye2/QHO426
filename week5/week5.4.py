def direction():
    steps = ["Move Forward", "Move Backward", "Turn Left" , "Turn Right"]
    return steps

def menu():
    print("Please select a direction:")
    steps = direction()
    for index in range(len(steps)):
        print(f"{index}: {steps[index]}")
    index = int(input("Where would you like to go? "))
    return steps[index]


def run_task():
    route=[]
    print("working out escape route")
    for items in range(5):
        route.append(menu())
        print(f"Escape route: {route}")


if __name__ == "__main__":
    run_task()
