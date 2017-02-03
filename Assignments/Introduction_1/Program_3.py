#Exponent Calculator MkIII
#3 Febuary 2017
#Maxwell Phillips
#C Block Programming
#-------------------
#Algorithm:
#1. Intructional Text
#2. Requests input for base
#3. Requests input for exponent
#4. Asks if you want to run again
#-------------------------------------------------------------------------------
#Instructional Text
print("Hello and welcome to the Exponent Calculator MkIII! Lets begin!")
print("To use this program, simply input a integer base and exponent.\n The computer will do the rest!")
#Calculator
continue_program = "y"
while continue_program == "y":
    base = int(input("Please input a base integer: "))
    exponent = int(input("Please input a exponent integer: "))
    result = str(base**exponent)
    print("\nThe result is: " + result + "!")
    continue_program = str(input("Would you like to run again?(y/n): "))

print("\nThanks for using! Bye!")
