# Function for title 
def title():
    print("The Quarterly Sales program")

# user input for each Q

quarters = [user_input_q1 = float(input("Enter sales for Q1: ")),
user_input_q2 = float(input("Enter sales for Q2: ")),
user_input_q3 = float(input("Enter sales for Q3: ")),
user_input_q4 = float(input("Enter sales for Q4: "))]

# Function for total
def q_total():
    total = sum(quarters)
    print("Total: " + str(total))
    
# Function for average 
def q_average():
    average = sum(quarters) / len(quarters)
    print("Average Quater: " + str(average))

# Function for lowest Q
def q_lowest():
    return 0

# Function for highest Q
def q_highest():
    return 0 

# Main function 
def main():
    title()
    q_total()
    q_average()

main()