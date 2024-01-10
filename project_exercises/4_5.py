import random

# TODO Function to roll dice, return value between 1-6
def rolldice():
    val = random.randint(1, 6)
    return val

# TODO While loop to continue the program 





# TODO Exit statement 



def main():
    while True:
        choice = input("Wanna roll the dice? (y/n)")
        if choice.lower() != 'y':
            print("Good bye!")
            break

        # Display title 
        print("Dice Roller")
        die1 = rolldice()
        die2 = rolldice()
        print(f"Die 1: {die1}")
        print(f"Die 2: {die2}")
        total = die1 + die2
        print(f"Total: {total}")

    # TODO Check the return and display special messages
        if total == 2: 
            print("Snake eyes!")
        elif total == 12:
            print("Boxcars!")

main()