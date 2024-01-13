print("Shipping Calculator")
print("=====================================================")

cost_of_items = float(input("Cost of items ordered: "))
shipping_less_than_30 = 5.95
shipping_between_30_and_49 = 7.95
shipping_between_50_and_74 = 9.95
shipping_more_than_75 = 0

if cost_of_items <= 30:
    shipping_cost = shipping_less_than_30
elif 30 < cost_of_items <= 49:
    shipping_cost = shipping_between_30_and_49
elif 50 <= cost_of_items <= 74:
    shipping_cost = shipping_between_50_and_74
else:
    shipping_cost = shipping_more_than_75

print(f"Shipping cost: ${shipping_cost:.2f}")
