print("Hike Calculator")

def convert_miles_to_feet(miles):
    feet = int(miles * 5280)
    return feet

def main():
    miles = float(input("Enter the number of miles walked: "))
    feet_walked = convert_miles_to_feet(miles)
    print(f"You walked {feet_walked} feet.")

if __name__ == "__main__":
    main()
