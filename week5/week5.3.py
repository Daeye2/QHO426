def direction():
    steps = ["Move Forward", "Move Backward", "Turn Left" , "Turn Right"]
    return steps

def menu():
    print("Please select a direction:")
    steps = direction()
    for index in range(len(steps)):
        print(f"{index}: {steps[index]}")

def run_task():
    menu()

if __name__ == "__main__":
    run_task()
