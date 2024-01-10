print("Calculate Change")
x = int(input("Enter the number of cents: "))
quarters = 25
dimes = 10
nickles = 5
pennies = 1

number_of_quarters = int((x - (x % quarters))/quarters)
money2 = x % quarters

number_of_dimes = int(money2 - (money2 % dimes))/dimes
money3 = money2 % dimes

number_of_nickles = int(money3 - (money3 % nickles))/nickles

pennies = money3 % nickles

print(f"Quarters: \t{round(number_of_quarters, 0)}")
print(f"Dimes: \t\t{round(number_of_dimes)}")
print(f"Nickles: \t{round(number_of_nickles)}")
print(f"Pennies: \t{round(pennies)}")