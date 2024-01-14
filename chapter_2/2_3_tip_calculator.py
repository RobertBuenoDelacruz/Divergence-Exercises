print("Tip Calculator\n")

cost_of_meal = float(input("Cost of meal?: "))
tip_percent = float(input("Tip Percent: "))

tip_amount = cost_of_meal * (tip_percent / 100)

print(f"Tip amount: {tip_amount:.2f}")
print(f"Total amount: {tip_amount + cost_of_meal:.2f}")

