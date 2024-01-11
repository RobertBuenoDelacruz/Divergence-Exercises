# Display title 
def title():
    print("Prime Number Checker")
   
# Factors 
def get_factors(num):
    factors = []
    for factor in range(1, num + 1):
        remainder = num % factor
        if remainder == 0:
            # i is a factor of num 
            factors.append(factor)
    # print(factors)
    return factors
        

# Get user input - valid user
def get_input():
    num = int(input("Please enter an interger between 1 and 5000: "))
    if num >= 1 and num <= 5000:
        # print("Valid input")
        return num 
    else:
        print("Invalid number. Please try again.")

# While loop to try again 

# Main function 

# Call function 
def main():
    while True: 
        title()
        num = get_input()
        factors = get_factors(num)
        if len(factors) == 2:
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number.")
            print(f"Factors of {num}: {factors}")

        another_num = input("Type another number? (y/n): ")
        if another_num.lower() != 'y':
            print("Bye!")
            break
main()