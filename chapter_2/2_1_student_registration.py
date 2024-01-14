print("Registration Form\n")

user_first_name = input("First name: ")
user_last_name = input("Last name: ")
user_birth_year = input("Birth year: ")

print(f"\nWelcome {user_first_name} {user_last_name}!")
print(f"Your registration is complete.")
print(f"Your temorary password is: {user_first_name}*{user_birth_year}")