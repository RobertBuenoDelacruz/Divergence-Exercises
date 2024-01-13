print("Registration Form")

user_first_name = (input("First name: "))
user_last_name = (input("Last name: "))
birth_year = (input("Birth year: "))

print(user_first_name + " " + user_last_name)
print("Your registration is complete.")
print("Your temporary password is: " + user_first_name + "*" + birth_year)