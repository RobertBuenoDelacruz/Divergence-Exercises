print("Pay Check Calculator\n")

hours_worked = float(input("Hours Worked: \t"))
hourly_rate = float(input("Hourly rate: \t"))

tax_rate = 0.18

gross_pay = hours_worked * hourly_rate
print(f"\nGross pay: \t{gross_pay:.2f}")

print(f"Tax rate: \t{tax_rate * 100:.0f}%")

tax_amount = gross_pay * (tax_rate / 100)
print(f"Tax amount: \t{tax_amount:.2f}")

take_home_pay = gross_pay - tax_amount
print(f"Take Home Pay: \t{take_home_pay:.2f}")




