def observe():
    observations = []

    for count in range (3):
        print("Please enter an observation ")
        observations.append(input())

    return observations

def remove_observation(observations):
    is_running = True
    while is_running:
        print("do you wish to remove any observation (yes/no)")
        response = input()

        if response == "yes":
            print("Which one to remove")
            observation = input()
            observations.remove(observation)
        else:
            is_running = False


def run_task3():
    observations = observe()
    remove_observation(observations)

    observation_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observation_set.add(data)

    for data in sorted(observation_set):
        print(f"{data[0]} observed {data[1]} times")

run_task3()

