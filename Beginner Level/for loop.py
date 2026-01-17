import random

# 1: Dice Rolling Simulation

count_6 = 0
count_1 = 0
two_6s_in_row = 0
previous_roll = 0

print("Dice Rolling Simulation:\n")

for i in range(20):
    roll = random.randint(1, 6)
    print("Roll", i + 1, ":", roll)

    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            two_6s_in_row += 1

    if roll == 1:
        count_1 += 1

    previous_roll = roll

print("\nDice Statistics:")
print("Rolled 6:", count_6, "times")
print("Rolled 1:", count_1, "times")
print("Two 6s in a row:", two_6s_in_row, "times")

# 2: Jumping Jacks Workout
print("\nJumping Jacks Workout:\n")

total_jumps = 0

for i in range(1, 11):
    total_jumps += 10
    print("You completed", total_jumps, "jumping jacks.")

    if total_jumps == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/y or no/n): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip == "yes" or skip == "y":
            print("You completed a total of", total_jumps, "jumping jacks.")
            break
    else:
        print(100 - total_jumps, "jumping jacks remaining.")
