def pattern():
    sequences = {
        "short sequence" : 3,
        "medium sequence" : 4,
        "long sequence" : 5,
    }

    return sequences

def display_keys(data):
    print("Keys: ")
    for key in data:
        print(key)

def display_values(data):
    print("Values: ")
    for value in data.values():
        print(value)

def display_pairs(data):
    print("Pairs: ")
    for key, value in data.items():
        print(f"{key}, {value}")

def run():
    data = pattern()
    print(f"Dictionary:\n{data}")
    display_keys(data)
    display_values(data)
    display_pairs(data)

run()