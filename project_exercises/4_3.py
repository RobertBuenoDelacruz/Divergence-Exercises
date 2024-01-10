# TODO: Title Feet and meters convertor 
def title():
    print("Feet and meters convertor")

# TODO: Conversion Menu 
def conversion_menu(): 
    print("a. Feet to Meters")
    print("b. Meters to Feet")
    print()

def feet_to_meters(meters):
    feet = float(meters / 0.3048)
    return feet

def meters_to_feet(feet):
    meters = float(feet * 0.3048)
    return meters

def main():
    title()
    conversion_menu()
    choice = input("a or b") 
    user_input = float(input("Enter number if miles:"))
    if choice == "a":
        result = feet_to_meters(user_input)
        print(str(round(result, 2)))
    elif choice == "b":
        result = meters_to_feet(user_input)
        print(str(round(result, 2)))
    else: 
        print("Entered wrong option")

if __name__ == "__main__":
    main()
    
    


