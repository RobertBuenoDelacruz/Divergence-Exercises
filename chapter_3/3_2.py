print("Tip calculator")

tip_15 = 0.15
tip_20 = 0.20
tip_25 = 0.25

cost_of_meal = float(input("Enter total amount of meal: "))


tip_amount = cost_of_meal * tip_15
total_cost_15 = round(tip_amount + cost_of_meal, 2)
print(total_cost_15)

tip_amount = cost_of_meal * tip_20
total_cost_20 = round(tip_amount + cost_of_meal, 2)
print(total_cost_20)

tip_amount = cost_of_meal * tip_25
total_cost_25 = round(tip_amount + cost_of_meal, 2)
print(total_cost_25)







