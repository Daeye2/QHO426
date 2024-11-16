def movements():
    path = ["Move Forward", 10 ,  "Move Backward", 5 ,  "Turn Left" , 3 ,  "Turn Right" , 1]
    return path

def run_task():
    print("Moving......")
    path = movements()
    #print(f"{path[0]} for {path[1]} steps")
    #print(f"{path[2]} for {path[3]} steps")
    #print(f"{path[4]} for {path[5]} steps")
    #print(f"{path[6]} for {path[7]} steps")

    for item in range(0,len(path), 2):
        print(f"{path[item]} for {item + 1} steps")

if __name__ == "__main__":
    run_task()
