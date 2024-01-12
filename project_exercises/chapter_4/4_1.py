# Make title 
print("Even or Odd Checker")

# TODO: Determine is number is even or odd

def check_even_or_odd(num):
    if num % 2 == 0:
        return "This number is even"
    else: 
        return "This number is odd"


# TODO: Validate code

def main():
    # TODO take user input
    user_input = int(input("Enter a number: "))
    # TODO call function
    
    print(check_even_or_odd(user_input))

main()
