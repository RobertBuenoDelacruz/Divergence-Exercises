# Display Title
print("Table of Powers")

# Get two inputs from user (start and stop number)

while True:
    start = int(input("Start number: "))
    stop = int(input("Stop number: "))

    # Validate User input
    # Make sure the user enters a start integer that’s less than the stop integer. 

    if(start < stop):
        # print("Valid Input")
        break
    else: 
        print("Start number should be lower than the stop number")

# If the user enters a start integer that’s greater than the stop integer, display an error message and give the user a chance to enter the integers again.
# Use a for loop to calculate and print the table
        
print("Number \t Square \t Cubed")

for i in range(start, stop + 1, 1): 
    print(f"{i} \t {i ** 2} \t {i ** 3}")


