print("Pay Check Calculator") 

hours_worked = float(input("Hours worked: "))
hourly_rate = float(input("Hourly rate: "))

tax_rate = 0.18

gross_pay = hours_worked * hourly_rate
tax_amount = gross_pay * (tax_rate / 100)
take_home_pay = gross_pay - tax_amount

print("Gross Pay: " + str(round(gross_pay, 2)))
print("Tax Rate: " + str(tax_rate))
print("Tax Amount: " + str(round(tax_amount, 2)))
print("Take Home Pay: " + str(round(take_home_pay, 2)))


