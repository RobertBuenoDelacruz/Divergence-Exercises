print("Tip Calculator")

cost_of_meal = float(input("Cost of meal: "))
tip_percent = float(input("Tip percent: "))

tip_amount = cost_of_meal * (tip_percent / 100)
total_amount = tip_amount + cost_of_meal

print("Tip amount: " + str(round(tip_amount, 2)))
print("Total amount: " + str(round(total_amount, 2)))