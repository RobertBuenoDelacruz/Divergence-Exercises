print("Letter Grade Conveter") 

choice = "y"
while choice.lower() == "y":
    score = int(input("Enter test score: "))
    if score >= 90: 
        print( "A")
         
    elif score >= 80:
        print("B")
         
    elif score >= 70: 
        print("C")
         
    elif score >= 60: 
        print("D")
        
    else: 
        print("F")
    choice = input("Would you like to enter another grade? (y/n)")
print("Bye")