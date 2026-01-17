print("1 List of Friends")
friends = ["Juveriya","Anzila", "Tazeen", "Husna", "Aman"]

name_length_tuples = []

for name in friends:
    name_length_tuples.append((name, len(name)))

print("Friends name and length:")
print(name_length_tuples)

print("===============================================================")
print("2 Trip Planning Track Expension")

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\nTotal Expenses:")
print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

if your_total > partner_total:
    print("You spent more money overall.")
elif partner_total > your_total:
    print("Your partner spent more money overall.")
else:
    print("Both spent the same amount.")

max_difference = 0
category_name = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > max_difference:
        max_difference = difference
        category_name = category

print("\nCategory with significant spending difference:")
print(category_name, "with a difference of", max_difference)
