def calculate_tip_cost():
    while True:
        try:
            cost_of_meal = float(input("Cost of meal: "))
            if cost_of_meal <= 0:
                print("Must be greater than 0. Please try again.")
                continue
            
            tip_percent = int(input("Tip percent: "))
            if tip_percent <= 0:
                print("Must be a valid integer greater than 0. Please try again.")
                continue
            
            tip_amount = round(cost_of_meal * (tip_percent / 100), 2)
            total_amount = round(cost_of_meal + tip_amount, 2)
            
            print("\nOUTPUT")
            print(f"Cost of meal: {cost_of_meal}")
            print(f"Tip percent: {tip_percent}%")
            print(f"Tip amount: {tip_amount}")
            print(f"Total amount: {total_amount}")
            
            break
        except ValueError as ve:
            print(ve)

if __name__ == "__main__":
    print("Tip Calculator")
    calculate_tip_cost()


