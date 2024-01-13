
def is_your_number_prime(input_number):
    
    if input_number <= 1: 
        return False
    for i in range(2, int(input_number ** 0.5) + 1):
        if input_number % i == 0:
            return False 
    # return input + " is a prime number."
    return True 

def main():
    print("Prime Number Checker")
    while True:
        user_input = int(input("Please enter interger between 1 and 5000: "))

        if is_your_number_prime(user_input):
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")
        
            
            choice = input("Try again? (y/n): ").lower()
            if choice != "y":
                print("Bye!")
                break
                

if __name__ == "__main__":
    main()




