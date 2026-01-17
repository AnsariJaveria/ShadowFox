#List
# Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Original Justice League:", justice_league)

# 1. Calculate the number of members
num_members = len(justice_league)
print("1 Number of members:", num_members)
print("======================================================================================")

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("2 After adding Batgirl and Nightwing:", justice_league)
print("======================================================================================")

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("3 After moving Wonder Woman to the beginning:", justice_league)
print("======================================================================================")

# 4. Separate Aquaman and Flash by placing Green Lantern between them
# Remove Flash and Green Lantern to avoid duplicate entries while reordering
justice_league.remove("Flash")
justice_league.remove("Green Lantern")

# Find index of Aquaman
index_aquaman = justice_league.index("Aquaman")

# Insert Green Lantern after Aquaman
justice_league.insert(index_aquaman + 1, "Green Lantern")

# Insert Flash after Green Lantern
justice_league.insert(index_aquaman + 2, "Flash")

print(" 4 After placing Green Lantern between Aquaman and Flash:", justice_league)
print("=================================================================================================")

# 5. Replace the list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("5 After forming a new team:", justice_league)
print("=================================================================================================")

# 6. Sort the Justice League alphabetically
justice_league.sort()
print("6 Justice League sorted alphabetically:", justice_league)
print("====================================================================================================")

print("Bonus:New leader (0th index):", justice_league[0])

