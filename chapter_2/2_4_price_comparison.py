print("Price Comparison\n")

price_of_64 = float(input("Price of 64 iz size: "))
price_of_32 = float(input("Price of 32 iz size: "))

price_per_oz_64 = price_of_64 / 64
price_per_oz_32 = price_of_32 / 32

print(f"\nPrice per oz (64 oz) : {price_per_oz_64:.2f}")
print(f"Price per oz (32 oz) : {price_per_oz_32:.2f}")
