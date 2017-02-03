#Two to a Power of Your Choosing Program
#3 Febuary 2017
#Maxwell Phillips
#C Block Programming
#-------------------
#Alogrithm:
#1. Instructional Text
#2. Requests a user input
#3. Calculates two to the power of that user's input
#4. Outputs result and asks if they wish to input another value
#5. If so, runs again, if not says bye and terminates program
#-------------------------------------------------------------------------------
#Instructional Text
print("Welcome to another exponent program! Lets do some stuff!")
print("This program will ask for a power of two, and then output the result.\n Lets try it out!")
#Begin calculations and input
continue_program = "y"
while continue_program == "y":
    n = int(input("What power of two do you wish to use?(Please use and integer): "))
    print("The answer is: " + str(2**n) + "!")
    continue_program = input("Do you wish to enter another value?(y/n): ")

print("\n Okay, thanks for using! Bye!")
