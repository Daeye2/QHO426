# Prompt the user for the number of steps to reach the target
target_steps = int(input("How far are we from the target? "))

# Count down from target_steps to 0
for steps_remaining in range(target_steps, 0, -1):
    print(f"{steps_remaining} Steps remaining!")

print(f"You've reached the target!")