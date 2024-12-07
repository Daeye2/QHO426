def observe():
    observations = []

    for count in range (7):
        print("Please enter an observation ")
        observations.append(input())

    return observations

def run_task2():
    print("Counting observations")
    observes = observe()

    observation_set = set()
    for observation in observes:
        data = (observation, observes.count(observation))
        observation_set.add(data)

    for data in observation_set:
        print(f"{data[0]} observed {data[1]} times")

run_task2()